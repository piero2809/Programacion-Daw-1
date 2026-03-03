#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# 1. CAMBIO: El modelo exacto que usaste
BASE_MODEL = "LiquidAI/LFM2.5-1.2B-Thinking"

# 2. CAMBIO: La carpeta exacta donde guardó el script de entrenamiento anterior
ADAPTER_PATH = "./LFM2.5-1.2B-Thinking-jvc-lora-cpu"

# Carpeta de salida para el modelo fusionado
OUT_PATH = ADAPTER_PATH + "-merged"

def main():
    if not os.path.isdir(ADAPTER_PATH):
        raise FileNotFoundError(
            f"No encuentro la carpeta del adaptador: {ADAPTER_PATH}\n"
            f"Asegúrate de que el entrenamiento terminó y creó esta carpeta."
        )

    print(f"Creando carpeta de salida: {OUT_PATH}")
    os.makedirs(OUT_PATH, exist_ok=True)

    use_cuda = torch.cuda.is_available()
    # En CPU usamos float32 para evitar errores de merge
    dtype = (torch.float16 if use_cuda else torch.float32)

    print("BASE_MODEL   :", BASE_MODEL)
    print("ADAPTER_PATH :", ADAPTER_PATH)
    print("OUT_PATH     :", OUT_PATH)
    print("CUDA         :", use_cuda, "| dtype:", dtype)

    print("Cargando modelo base...")
    # 3. CAMBIO: trust_remote_code=True es OBLIGATORIO para LiquidAI
    base = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype=dtype,
        device_map="auto" if use_cuda else {"": "cpu"},
        trust_remote_code=True 
    )

    print("Cargando tokenizer...")
    tok = AutoTokenizer.from_pretrained(BASE_MODEL, use_fast=True, trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token

    print("Cargando adaptadores LoRA...")
    # Se carga el modelo PEFT sobre la base
    model = PeftModel.from_pretrained(base, ADAPTER_PATH)

    print("Fusionando (merge_and_unload)...")
    # Esto une los pesos del adaptador al modelo base permanentemente
    merged = model.merge_and_unload()

    try:
        merged.config.use_cache = True
    except Exception:
        pass

    print("Guardando modelo fusionado...")
    merged.save_pretrained(OUT_PATH, safe_serialization=True)

    print("Guardando tokenizer...")
    tok.save_pretrained(OUT_PATH)

    print("✅ Modelo fusionado guardado en:", OUT_PATH)


if __name__ == "__main__":
    main()