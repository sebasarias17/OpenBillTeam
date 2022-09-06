import cv2 as cv

# Se inicia la cámara
cam_port = 0
cam = cv.VideoCapture(0, cv.CAP_DSHOW)

# Lee la entrada que recibe la cámara
result, image = cam.read()

if result:
    cv.imshow("Camara", image)
    cv.imwrite("pics/pic.png", image)

    # Para salir de la preview de la foto
    cv.waitKey(0)
    cv.destroyWindow("Camara")
else: 
    print("Error!")