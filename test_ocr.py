import pytesseract
from PIL import Image

# Tesseract path (important for Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("test.png")

text = pytesseract.image_to_string(img)

print("===== OCR RESULT =====")
print(text)