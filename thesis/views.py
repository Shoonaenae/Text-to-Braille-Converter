from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from PIL import Image

from thesis.utils.braille_utils import braille_to_image, text_to_braille, translate_to_braille
from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont

import base64
import numpy as np
import pytesseract


# kaye's directory
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)

myconfig = r"--oem 3 --psm 3"
# -l chi_tra+english

braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', ' ': '⠀', '.': '⠲', ',': '⠂',
    '?': '⠦', '!': '⠖', "'": '⠄', '-': '⠤', '(': '⠐⠣', ')': '⠐⠜'
}


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
        img = Image.open(image)

        lang = request.POST["language"]
        
        # Calculate the new size while maintaining the aspect ratio
        if lang == 'eng':
            width, height = img.size
            aspect_ratio = width / height
            new_width = 834
            new_height = int(new_width / aspect_ratio)
            new_size = (new_width, new_height)
            
            # Resize the image
            resized_image = img.resize(new_size)
            text = pytesseract.image_to_string(resized_image, lang = lang, config = myconfig)
            
            # return text to html
            return render(request, "home.html", {"ocr": text, "image": image_base64})
        elif lang == 'chi_tra' or lang == "eng+chi_tra":
            width, height = img.size
            aspect_ratio = width / height
            new_width = 834
            new_height = int(new_width / aspect_ratio)
            new_size = (new_width, new_height)
            
            # Resize the image
            resized_image = img.resize(new_size)

            # Convert the image to grayscale
            grayscale_image = resized_image.convert('L')

            text = pytesseract.image_to_string(grayscale_image, lang = lang, config = myconfig)

            # return text to html
            return render(request, "home.html", {"ocr": text, "image": image_base64})

    return render(request, "home.html")


    
def convert_to_braille_image(request):
    if request.method == 'POST':
        text = request.POST['brailleText']
        braille = text_to_braille(text)
        braille_to_image(braille)
        return render(request, 'home.html', {'image_path': braille})
    else:
        return render(request, 'home.html')
def translate(request):
    if request.method == 'POST':
        text = request.POST['ctext']
        cbraille = translate_to_braille(text)
        braille_to_image(cbraille)
        return render(request, 'home.html', {'text': text, 'cbraille': cbraille})
    else:
        return render(request, 'home.html')