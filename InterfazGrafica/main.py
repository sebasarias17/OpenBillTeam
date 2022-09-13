#@autor: Sebastian Arias Usma

import sys
from ui_design import *
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtGui import QPixmap
import cv2 as cv

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

        #Boton encender camara
        self.logic = 0
        self.value = 1
        self.ui.btn_on.clicked.connect(self.act_camara)

        #Boton capturar
        self.ui.btn_capturar.clicked.connect(self.capturar)

        ##Boton apagar camara
        self.ui.btn_off.clicked.connect(self.off_cam)

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
        fname = QFileDialog.getOpenFileName(self, "Open File","","PNG(*.png);;JPEG(*.jpeg);;JPG(*.jpg)")
        
        self.pixmap = QPixmap(fname[0])
        self.ui.prev_foto.setPixmap(self.pixmap)

    #metodo refrescar imagen
    def refrescar_img(self):
        self.ui.prev_foto.clear()

    ##metodo buscar archivos
    def search_file(self):
        fname = QFileDialog.getOpenFileName(self, "Open File","","PDF(*.pdf)")

        self.pixmap = QPixmap(fname[0])
        self.ui.prev_file.setPixmap(self.pixmap)
        if fname:
            self.ui.file_path.setText(str(fname))

    #metodo refrescar archivos
    def refrescar_file(self):
        self.ui.prev_file.clear()
        self.ui.file_path.clear()

    ##metodo prender camara
    def act_camara(self):
        self.logic = 1
        self.cap = cv.VideoCapture(0)
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret == True:
                self.display(frame, 1)
                cv.waitKey()

                if(self.logic ==2):
                    self.value = self.value+1
                    cv.imwrite("C:/Users/Usuario/OneDrive/Escritorio/OpenBill/capturas/%s.png"%(self.value),frame)

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
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())