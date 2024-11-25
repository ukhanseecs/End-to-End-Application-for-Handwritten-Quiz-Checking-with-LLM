import cv2
from PIL import Image
import pytesseract

# Load the image
image_path = 'images/clear.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Preprocess the image (e.g., binarization)
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

# Save the processed image temporarily
processed_image_path = 'processed_image.jpg'
cv2.imwrite(processed_image_path, binary_image)

# Perform OCR on the processed image
text = pytesseract.image_to_string(Image.open(processed_image_path), lang='eng')

print("Extracted Text from Processed Image:")
print(text)
