from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from PIL import Image
from googletrans import Translator
from .braille_converter import translateToBraille

import base64
import numpy as np
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = (
    r"A:\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)

myconfig = r"-l eng+chi_sim"

# Create your views here.
def index(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]

            # encode image to base64 string
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "no image is uploaded"
            )

            return render(request, "home.html")

        # lang = request.POST["language"]    
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