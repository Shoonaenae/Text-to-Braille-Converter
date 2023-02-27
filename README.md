# Text-to-Braille-Converter
Text to Braille with OCR 

### requirements
make sure to install the following: --> better on a virtual environment
1. [tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and add it to your environment variables
2. numpy ```pip install numpy```
3. PIL ```pip install PIL```
4. cv2 ```pip install opencv-python```
5. download the trained datasets used below and make sure to place it inside the trained data folder of the tesseract ocr installation location.
- [simplified chinese](https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata)
- [vertical simplified chinese](https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim_vert.traineddata)
- [traditional chinese](https://github.com/tesseract-ocr/tessdata/blob/main/chi_tra.traineddata)
- [vertical traditional chinese](https://github.com/tesseract-ocr/tessdata/blob/main/chi_tra_vert.traineddata)