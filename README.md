# Text-to-Braille-Converter
Text to Braille with OCR 

### requirements
make sure to install the following: --> better on a virtual environment
1. [tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and add it to your environment variables
2. numpy ```pip install numpy```
3. PIL ```pip install PIL```
4. [simplified chinese trained dataset](https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata). make sure to place it inside the trained data folder of the tesseract ocr installation location.

### ocr
supports the following languages:
- english
- chinese _simplified_

### how to use the website
1. upload an __image__ 
2. select the __language__
3. get the text
