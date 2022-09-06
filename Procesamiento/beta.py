import pytesseract as pt
import PIL
from PIL import Image
import cv2 as cv

cam_port = 0
cam = cv.VideoCapture(0, cv.CAP_DSHOW)

result, image = cam.read()

if result:
    cv.imshow("pic", image)
    cv.imwrite("pics/recognizedPic.png", image)
    cv.waitKey(0)
    cv.destroyWindow("pic")
else:
    print("No pude reconocer nada :(")

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('pics/recognizedPic.png')
text = pt.image_to_string(img)

print("Reconoci: \n", text)