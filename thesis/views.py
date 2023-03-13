from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from PIL import Image
from .braille_converter import translateToBraille

import base64
import numpy as np
import pytesseract
import cv2

# kaye's
pytesseract.pytesseract.tesseract_cmd = (
    r"X:\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)

myconfig = r"-l chi_tra+english"

# Create your views here.
def resize(im, newWidth):
    width, height = im.size
    ratio = height / width
    newHeight = int(ratio * newWidth)
    resizedImage = im.resize((newWidth, newHeight))

    return resizedImage

def index(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]

            # encode image to base64 string
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "no image is  uploaded"
            )

            return render(request, "home.html")
  
        img = np.array(Image.open(image))
        text = pytesseract.image_to_string(img, config = myconfig)

        # return text to html
        return render(request, "home.html", {"ocr": text, "image": image_base64})

    return render(request, "home.html")

def convert_text_to_braille(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        braille_text = translateToBraille(input_text)
        return render(request, 'home.html', {'braille_text': braille_text})
    else:
        return render(request, 'home.html')