import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        # 1) TRY direct text first (IMPORTANT)
        page_text = page.get_text()

        if page_text.strip():
            text += page_text + "\n"
        else:
            # 2) fallback OCR only if needed
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            text += pytesseract.image_to_string(img) + "\n"

    return text