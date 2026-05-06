import pytesseract
from PIL import Image, ImageOps, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess(img):
    img = ImageOps.grayscale(img)
    img = img.resize((img.width * 2, img.height * 2))
    img = img.filter(ImageFilter.SHARPEN)
    return img

def extract_text(image_path):
    img = Image.open(image_path)
    img = preprocess(img)

    config = "--psm 6"
    return pytesseract.image_to_string(img, config=config)