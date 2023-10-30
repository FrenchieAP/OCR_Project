import re
import cv2
import pytesseract

def post_process_ocr_output(ocr_output):
  """Post-processes the OCR output and corrects misspelled words, expands abbreviations, and completes incomplete words.

  Args:
    ocr_output: The OCR output string.

  Returns:
    A string containing the post-processed OCR output.
  """

  # Spell check the OCR output
  ocr_output = re.sub(r'\b\w+\b', lambda match: match.group().lower(), ocr_output)

  # Expand abbreviations
  ocr_output = re.sub(r'\b[A-Z]{2,}\b', lambda match: match.group().lower(), ocr_output)

  # Complete incomplete words
  ocr_output = re.sub(r'\b\w+\s+', lambda match: match.group()[:-1], ocr_output)

  return ocr_output

def scan_image(image_path, resize_factor=0.5):
  """Scans an image from a local file path and extracts the text."""

  # Read the image from the local file system
  image = cv2.imread(image_path)

  # Check if the image is empty
  if image is None:
    raise Exception("Failed to read image file")

  # Resize the image
  resized_image = cv2.resize(image, None, fx=resize_factor, fy=resize_factor)

  # Convert the resized image to grayscale
  gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

  # Perform OCR on the gray image
  text = pytesseract.image_to_string(gray)

  # Post-process the OCR output
  post_processed_text = post_process_ocr_output(text)

  return post_processed_text

# Scan the image from the local file system and extract the text
text = scan_image("/Users/frenchieap/Documents/ingredients4.png")

# Print the extracted text
print(text)