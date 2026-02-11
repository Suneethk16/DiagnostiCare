from pypdf import PdfReader
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image
import io


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract text from PDF.
    1. Try native text extraction
    2. If empty, fallback to OCR
    """

    # -------- Try normal PDF text extraction --------
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # -------- If text exists, return it --------
    if text.strip():
        return text

    # -------- OCR fallback for scanned PDFs --------
    images = convert_from_bytes(pdf_bytes)

    ocr_text = ""
    for img in images:
        ocr_text += pytesseract.image_to_string(img)

    return ocr_text
