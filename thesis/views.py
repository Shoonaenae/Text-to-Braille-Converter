from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from PIL import Image
from .braille_converter import translateToBraille

import base64
import numpy as np
import pytesseract

# kaye's directory
pytesseract.pytesseract.tesseract_cmd = (
    r"X:\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)

myconfig = r"-l chi_tra+english"

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
  
        #img = np.array(Image.open(image))
        img = Image.open(image)
        
        # Calculate the new size while maintaining the aspect ratio
        width, height = img.size
        aspect_ratio = width / height
        new_width = 403
        new_height = int(new_width / aspect_ratio)
        new_size = (new_width, new_height)

        # Resize the image
        resized_image = img.resize(new_size)

        # Convert the image to grayscale
        # grayscale_image = resized_image.convert('L')

        text = pytesseract.image_to_string(resized_image, config = myconfig)

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