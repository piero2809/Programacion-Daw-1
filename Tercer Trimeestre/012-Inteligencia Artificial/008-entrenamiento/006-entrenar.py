#!/usr/bin/env python3
import os
import torch
from datetime import datetime

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model


# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------
DATA_FILE = "004-preentrenamiento relleno.jsonl"
MODEL_NAME = "LiquidAI/LFM2.5-1.2B-Thinking"
OUTPUT_DIR = "./LFM2.5-1.2B-Thinking-jvc-lora-cpu"

MAX_LENGTH = 128
NUM_EPOCHS = 3
LR = 2e-4
BATCH_SIZE = 1
GRAD_ACCUM = 4


def main():
    start_dt = datetime.now()

    print("🚀 Iniciando entrenamiento...")
    
    if not os.path.isfile(DATA_FILE):
        raise FileNotFoundError(f"No encuentro el archivo: {DATA_FILE}")

    # 1. Detectar CPU vs GPU
    if torch.cuda.is_available():
        device = "cuda"
        print("💻 MODO GPU DETECTADO.")
    else:
        device = "cpu"
        print("⚠️ MODO CPU: Se desactivará device_map='auto' para evitar errores 'meta'.")

    # ------------------------------------------------------------
    # Tokenizer
    # ------------------------------------------------------------
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # ------------------------------------------------------------
    # Modelo (CORREGIDO PARA CPU)
    # ------------------------------------------------------------
    print("⬇️ Cargando modelo...")
    
    # Configuración específica para evitar el error "meta device"
    model_kwargs = {
        "trust_remote_code": True,
        "torch_dtype": torch.float32, # CPU DEBE usar float32 obligatoriamente
    }

    if device == "cuda":
        # Si hay GPU, usamos optimizaciones
        model_kwargs["device_map"] = "auto"
        model_kwargs["torch_dtype"] = torch.float16
    else:
        # Si es CPU, NO usamos device_map="auto" ni low_cpu_mem_usage
        # Esto fuerza a que el modelo se cargue real en la RAM
        model_kwargs["device_map"] = None 
        model_kwargs["low_cpu_mem_usage"] = False

    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, **model_kwargs)

    # Si estamos en CPU, asegurarnos de que el modelo esté ahí
    if device == "cpu":
        model.to("cpu")
        model.config.use_cache = False # Ahorra RAM

    # Gradient checkpointing solo ayuda si hay GPU o memoria muy justa
    if device == "cuda":
        model.gradient_checkpointing_enable()

    # ------------------------------------------------------------
    # LoRA
    # ------------------------------------------------------------
    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules="all-linear",
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # ------------------------------------------------------------
    # Dataset
    # ------------------------------------------------------------
    raw_dataset = load_dataset("json", data_files=DATA_FILE, split="train")

    def qa_to_text(example):
        q = str(example.get("question", ""))
        a = str(example.get("answer", ""))
        return {"text": f"User: {q}\nAssistant: {a}"}

    text_dataset = raw_dataset.map(qa_to_text)

    def tokenize_fn(batch):
        out = tokenizer(
            batch["text"],
            truncation=True,
            max_length=MAX_LENGTH,
            padding="max_length",
        )
        out["labels"] = out["input_ids"].copy()
        return out

    tokenized_dataset = text_dataset.map(
        tokenize_fn,
        batched=True,
        remove_columns=text_dataset.column_names,
    )

    # ------------------------------------------------------------
    # Argumentos de Entrenamiento
    # ------------------------------------------------------------
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        logging_steps=5,
        save_steps=100,
        # CRÍTICO PARA CPU:
        fp16=(device == "cuda"), # False en CPU
        bf16=False,
        use_cpu=(device == "cpu"),
        dataloader_pin_memory=False, # Evita errores de paginación en CPU
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    print("🚂 Entrenando...")
    trainer.train()
    
    print(f"💾 Guardando en {OUTPUT_DIR}")
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("✅ ¡Listo!")

if __name__ == "__main__":
    main()