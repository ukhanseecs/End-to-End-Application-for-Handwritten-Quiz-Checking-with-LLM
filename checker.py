import cv2
import pytesseract
from PIL import Image
import json

def preprocess_image(image_path):
    # Preprocess the image by converting it to grayscale and applying a binary threshold.
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    _, thresholded = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    return thresholded

def extract_text(image_path):
    # Extract text from an image using Tesseract OCR.
    preprocessed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(preprocessed_image, lang="eng")
    return text

def save_text_to_json(text_data, output_path):
    # Save the extracted text data to a JSON file.
    with open(output_path, "w") as json_file:
        json.dump(text_data, json_file)
