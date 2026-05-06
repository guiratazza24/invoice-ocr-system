from pdf_ocr import pdf_to_text
from cleaner import clean_text
from parser import extract_invoices
import json

raw_text = pdf_to_text("pdfs/facture.pdf")
clean = clean_text(raw_text)

invoices = extract_invoices(clean)

print(json.dumps(invoices, indent=2, ensure_ascii=False))