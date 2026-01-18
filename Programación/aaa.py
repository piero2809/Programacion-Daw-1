# guardar como generar_pdf_instalacion.py y ejecutar con python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

doc_path = "Instalacion_Sistemas_resuelto_por_piero.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCenter', parent=styles['Heading1'], alignment=TA_CENTER))
styles.add(ParagraphStyle(name='Question', parent=styles['Normal'], fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='Answer', parent=styles['Normal'], leftIndent=12, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Small', parent=styles['Normal'], fontSize=9))

story = []
story.append(Paragraph("Instalación de sistemas operativos — Respuestas", styles['TitleCenter']))
story.append(Spacer(1, 12))
story.append(Paragraph("Documento: Respuestas a los ejercicios teóricos", styles['Normal']))
story.append(Paragraph("Autor: Piero Funes (generado por ChatGPT)", styles['Small']))
story.append(Spacer(1, 24))

q_and_a = [
    ("1. Define qué es un sistema operativo y explica sus funciones principales.", "Un sistema operativo (SO) es..."),
    # Añade aquí todas las preguntas y respuestas exactamente como las di arriba.
]

for q, a in q_and_a:
    story.append(Paragraph(q, styles['Question']))
    story.append(Spacer(1, 4))
    for part in a.split("\n"):
        story.append(Paragraph(part, styles['Answer']))
    story.append(Spacer(1, 12))

doc = SimpleDocTemplate(doc_path, pagesize=A4, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
doc.build(story)
print("PDF creado:", doc_path)
