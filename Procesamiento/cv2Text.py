import cv2
import pytesseract
import numpy as np
import csv
#import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('pics/facturaMano.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Para hacerlo en escala de grises
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Para hacerlo en blanco y negro 
#(thresh, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#print(pytesseract.image_to_string(img))

# Detectar caracteres
#hImg, wImg,_ = img.shape
#boxes = pytesseract.image_to_boxes(img)
#for b in boxes.splitlines():
#    b = b.split(' ')
#    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#    cv2.rectangle(img, (x, hImg-y-55), (w, hImg-y), (158, 240, 47), 3)
#    cv2.putText(img, b[0], (x+20, hImg-y+35), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

# Detectar palabras
hImg, wImg,_ = img.shape
# Para escala de grises
#hImg, wImg = img.shape
#cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img)

strLine, headLine = "", ""
state = False

for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        if len(b) == 12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (x+w, h+y), (158, 240, 47), 3)
            cv2.putText(img, b[11], (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            #print(b[11])
            if state == False:
                headLine += b[11] + ","
                if b[11] == "Total":
                    state = True
            if state == True:
                if b[11] != "Total":
                    if b[11] == "*" or b[11] == "x":
                        strLine = strLine[:-1]
                        strLine += '\n'
                    else:
                        strLine += b[11] + ","

# Formatear strLine, headLine para convertirlo en lista
headLine = headLine[:-1].split(',')
strLine = strLine.splitlines()
# Solo es para eliminar ese WorBRrRPRN todo extraño que sale por ahí idk
if len(strLine) != 0:
    strLine.pop()

#print(headLine)
#print(strLine)

rows = []

for x in strLine:
    lista = x.split(',')
    rows.append(lista)


print(headLine)
print(rows)

with open('resultado.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headLine)
    writer.writerows(rows)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.imwrite('pics/resultado.png', img)
