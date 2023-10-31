import logging
from paddleocr import PaddleOCR, draw_ocr

# Disable debug and info messages
logger = logging.getLogger('ppocr')
logger.setLevel(logging.ERROR)

ocr = PaddleOCR()

# Scan the image and extract the text
text = ocr.ocr("/Users/frenchieap/Documents/ingredients.jpeg")

# Process each line of text and print it
for line_info in text:
    line_text = " ".join([str(word_info[-1]) for word_info in line_info])
    print(line_text)
