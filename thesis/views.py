from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from PIL import Image

import base64
import numpy as np
import pytesseract
import re 

pytesseract.pytesseract.tesseract_cmd = (
    r"A:\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)

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

        lang = request.POST["language"]    
        img = np.array(Image.open(image))
        text = pytesseract.image_to_string(img, lang = lang)
        string = ""

        for n in re.findall(r"[\u4e00-\u9fff]+", text):
            string = string + n

        # return text to html
        return render(request, "home.html", {"ocr": text, "image": image_base64})

    return render(request, "home.html")