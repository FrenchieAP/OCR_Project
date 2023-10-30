import cv2
import pytesseract

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

  return text

# Scan the image from the local file system and extract the text
text = scan_image("/Users/frenchieap/Documents/ingredients4.png")

# Print the extracted text
print(text)