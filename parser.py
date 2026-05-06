import re

def safe_find(pattern, text):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None

def extract_invoices(text):
    blocks = text.split("Facture")

    results = []

    for block in blocks:
        if len(block.strip()) < 20:
            continue

        data = {
            "invoice_number": safe_find(r'numero_facture"\s*:\s*"([^"]+)"', block),
            "date": safe_find(r'date"\s*:\s*"([^"]+)"', block),
            "client": safe_find(r'client"\s*:\s*"([^"]+)"', block),
            "company": safe_find(r'ste_vente"\s*:\s*"([^"]+)"', block),
            "ht": safe_find(r'montant_ht"\s*:\s*([0-9.]+)', block),
            "ttc": safe_find(r'montant_ttc"\s*:\s*([0-9.]+)', block),
            "tva": safe_find(r'tva_19"\s*:\s*([0-9.]+)', block),
        }

        results.append(data)

    return results