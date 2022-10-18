#@autor: Sebastian Arias Usma
# Librerías para gestión de rutas y archivos
import sys
import os
# Librerías para la interfaz gráfica
from ui_design import *
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtGui import QPixmap
# Librerías para webcam y procesamiento de las imágenes
from re import L
import cv2
from cv2 import threshold
import numpy as np
from imutils.perspective import four_point_transform
import pytesseract
# Librerías para la conexión y gestión con la base de datos
import pymongo
# Librería para pdf
from pdf2image import convert_from_path

# cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

count = 0
scale = 0.5

font = cv2.FONT_HERSHEY_SIMPLEX

WIDTH, HEIGHT = 1920, 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Eliminamos la barra de titulo - opaciodad
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #Realizamos el SizeGrip
        self.gripSize =10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #Movemos la ventana
        self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

        #Acceder a las paginas
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.inicio))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.capturar))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.selec_foto))
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.selec_archivo))
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ajustes))

        #Botones para refrecar
        self.ui.bnt_refrescar.clicked.connect(self.refrescar_img)
        self.ui.btn_volver3.clicked.connect(self.refrescar_file)

        #Botones pagina seleccionar foto
        self.ui.btn_search.clicked.connect(self.search_foto)

        #Botones pagina seleccionar archivo
        self.ui.btn_search2.clicked.connect(self.search_file)

        #Boton seleccionar path para capturas
        self.ui.btn_carpeta.clicked.connect(self.obtener_path)

        #Boton encender camara
        self.logic = 0
        self.count = 1
        self.ui.btn_on.clicked.connect(self.act_camara)

        #Boton capturar
        self.ui.btn_capturar.clicked.connect(self.capturar)

        ##Boton apagar camara
        self.ui.btn_off.clicked.connect(self.off_cam)

        # Boton procesar
        self.ui.btn_transcribir.clicked.connect(self.transcript)
        # Boton procesar imagen seleccionada
        self.ui.btn_seleccionar.clicked.connect(self.transcriptSeleccionar)
        # Boton procesar pdf 
        self.ui.btn_aceptar.clicked.connect(self.pdfAnalysis)
        #Control de la barra de titulos
        self.ui.btn_segundoplano.clicked.connect(self.admin_btn_segundoplano)
        self.ui.btn_minimizar.clicked.connect(self.admin_btn_minimizar)
        self.ui.btn_maximizar.clicked.connect(self.admin_btn_maximizar)
        self.ui.btn_cerrar.clicked.connect(lambda: self.close())
        self.ui.btn_minimizar.hide()

        #menu lateral
        self.ui.btn_menu.clicked.connect(self.gestionar_menu)
        
    def admin_btn_segundoplano(self):
        self.showMinimized()

    def admin_btn_minimizar(self):
        self.showNormal()
        self.ui.btn_minimizar.hide()
        self.ui.btn_maximizar.show()
    
    def admin_btn_maximizar(self):
        self.showMaximized()
        self.ui.btn_maximizar.hide()
        self.ui.btn_minimizar.show()
    
    def gestionar_menu(self):
        if True:
            width = self.ui.frame.width()
            normal = 0
            if width == 0:
                extender = 250
            else: 
                extender = normal
                
            self.animacion = QPropertyAnimation(self.ui.frame, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    
    ##metdo ResizeGrip
    def resizeEvent(self, event):
        rect= self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    
    ##metodo mover ventana
    def  mousePressEvent(self, event):
        self.clickPosition= event.globalPos()
    
    def mover_ventana(self,event):
        if self.isMaximized == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.acept()
        
        if event.globalPos().y()<=20:
            self.showMaximized()
        else:
            self.showNormal()
            
    ##metodo buscar foto
    def search_foto(self):
        global rutaFoto
        fname = QFileDialog.getOpenFileName(self, "Open File","","PNG(*.png);;JPEG(*.jpeg);;JPG(*.jpg)")
        rutaFoto = fname[0]
        self.pixmap = QPixmap(fname[0])
        self.ui.prev_foto.setPixmap(self.pixmap)

    #metodo refrescar imagen
    def refrescar_img(self):
        self.ui.prev_foto.clear()

    ##metodo buscar archivos
    def search_file(self):
        global rutaFile
        fname = QFileDialog.getOpenFileName(self, "Open File","","PDF(*.pdf)")
        rutaFile = fname[0]
        self.pixmap = QPixmap(fname[0])
        self.ui.prev_file.setPixmap(self.pixmap)
        if fname:
            self.ui.file_path.setText(str(fname))

    #metodo refrescar archivos
    def refrescar_file(self):
        self.ui.prev_file.clear()
        self.ui.file_path.clear()


    #metodo obtener path 
    def obtener_path(self):
        self.ruta = QFileDialog.getExistingDirectory(self,caption = "Select a Folder" )

    ##metodo prender camara
    def act_camara(self):
        self.logic = 1
        self.cap = cv2.VideoCapture(0)
        while(self.cap.isOpened()):
            #ret, frame = self.cap.read()
            global frame, warped, processed
            _, frame = self.cap.read()
            # cambiar si la cámara está rotada 180 grados, sino, parchis
            frame = cv2.rotate(frame, cv2.ROTATE_180)
            frame_copy = frame.copy()
            
            self.scan_detection(frame_copy)
            warped = four_point_transform(frame_copy, document_contour.reshape(4,2))
            processed = self.image_processing(warped)

            #self.center_text(frame, "Scan Saved")
            #cv2.imshow("input", cv2.resize(frame, (int(scale * WIDTH), int(scale * HEIGHT))))
            #cv2.waitKey(500)

            self.display(processed, 1)
            cv2.waitKey()

            if(self.logic ==2):   
                self.count += 1             
                cv2.imwrite(os.path.join(self.ruta,"%s.png")%(self.count),processed)
                self.logic = 1
    
    #metodo para capturar
    def capturar(self):
        self.logic = 2

    ##metodo desplegar imagen
    def display(self,img,window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2] ==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        outImage = QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        outImage = outImage.rgbSwapped()

        if window ==1:
            self.ui.camara.setPixmap(QPixmap.fromImage(outImage))
            self.ui.camara.setScaledContents(True)

    ##metodo apagar camara
    def off_cam(self):
        self.terminar = self.cap.release()
        self.ui.camara.clear()

    ##metodo de transcripción
    def transcript(self):
        file = open('output/recognized_' + str(self.count - 1) + '.txt', 'w')
        ocr_text = pytesseract.image_to_string(warped)
        #print(ocr_text)
        file.write(ocr_text)
        file.close()

        self.center_text(frame, "Text Saved")
        """ cv2.imshow("input", cv2.resize(frame, (int(scale * WIDTH), int(scale * HEIGHT))))
        cv2.waitKey(500) """
        self.display(frame, 1)
        cv2.waitKey()

    def transcriptSeleccionar(self):
        ruta = cv2.imread(rutaFoto)
        file = open('output/recognized_' + str(self.count - 1) + '.txt', 'w')
        frame_copy = ruta.copy()
        
        #self.scan_detection(frame_copy)
        #warped = four_point_transform(frame_copy, document_contour.reshape(4,2))
        processed = self.image_processing(frame_copy)
        ocr_text = pytesseract.image_to_string(processed)

        #print(ocr_text)
        file.write(ocr_text)
        file.close()

        self.center_text(frame_copy, "Text Saved")
        """ cv2.imshow("input", cv2.resize(frame_copy, (int(scale * WIDTH), int(scale * HEIGHT))))
        cv2.waitKey(500)  """
        self.display(frame_copy, 1)
        cv2.waitKey()

    def image_processing(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        return threshold

    def scan_detection(self, image):
        global document_contour
        document_contour = np.array([[0, 0], [WIDTH, 0], [WIDTH, HEIGHT], [0, HEIGHT]])

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        max_area = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000:
                peri = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.015 * peri, True)
                if area > max_area and len(approx) == 4:
                    document_contour = approx
                    max_area = area
        
        cv2.drawContours(frame, [document_contour], -1, (0, 255, 0), 3)

    def center_text(self, image, text):
        text_size = cv2.getTextSize(text, font, 2, 5)[0]
        text_x = (image.shape[1] - text_size[0]) // 2
        text_y = (image.shape[0] + text_size[1]) // 2
        cv2.putText(image, text, (text_x, text_y), font, 2, (255, 0, 255), 5, cv2.LINE_AA)
    
    def pdfAnalysis(self):
        images = convert_from_path(rutaFile, last_page=5)
        # Convierte el documento pdf a fotos
        # Hay que limitar esta chimbada a 5 fotos máximo
        for i in range(len(images)):
            # Save pages as images in the pdf
            images[i].save('output/pdf/page'+ str(i) +'.jpg', 'JPEG')
        
        if len(images) > 4:
            print('PDF muy grande para ser analizado!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())