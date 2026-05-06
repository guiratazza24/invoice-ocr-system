import os
import json

from pdf_ocr import pdf_to_text
from cleaner import clean_text
from parser import extract_invoices


PDF_FOLDER = "pdfs"
OUTPUT_FILE = "output.json"

all_results = []

# check folder exists
if not os.path.exists(PDF_FOLDER):
    print("ERROR: pdfs folder not found")
    exit()

# loop all files in folder
for filename in os.listdir(PDF_FOLDER):

    if filename.endswith(".pdf"):

        file_path = os.path.join(PDF_FOLDER, filename)

        print(f"\nProcessing: {filename}")

        try:
            # 1. OCR PDF
            raw_text = pdf_to_text(file_path)

            # 2. clean text
            clean = clean_text(raw_text)

            # 3. extract structured data
            invoices = extract_invoices(clean)

            # 4. add filename
            for inv in invoices:
                inv["source_file"] = filename
                all_results.append(inv)

        except Exception as e:
            print(f"Error with {filename}: {e}")

# save results
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)

print("\nDONE ✅ All invoices processed")
print(f"Saved to: {OUTPUT_FILE}")