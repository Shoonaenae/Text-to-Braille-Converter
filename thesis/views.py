from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from PIL import Image
from googletrans import Translator

import base64
import numpy as np
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = (
    r"A:\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)

myconfig = r"-l eng+chi_sim"

# Create your views here.

def say_hello(request):
    return HttpResponse("hello world")

    return render(request, "home.html")