from PySide6.QtWidgets import QDialog, QLabel
from PySide6.QtGui import QPixmap, QImage
from ui.ui_register import Ui_Register
from func.mysql import Mysql
from captcha.image import ImageCaptcha
import rc_resource
import matplotlib.pyplot as plt
import numpy as np 
import random, string

def pil_image_to_qimage(pil_image):
    """
    将PIL.Image.Image类型的图像转换为QImage类型
    """
    if pil_image.mode == "RGB":
        width, height = pil_image.size
        image_data = np.array(pil_image).astype(np.uint8)
        image_data = image_data[:, :, ::-1].copy()
        qimage = QImage(image_data.data, width, height, QImage.Format_RGB888)
        return qimage
    elif pil_image.mode == "L":
        width, height = pil_image.size
        image_data = np.array(pil_image).astype(np.uint8)
        qimage = QImage(image_data.data, width, height, QImage.Format_Index8)
        return qimage
    else:
        raise ValueError("不支持的PIL图像模式")

class Register(QDialog):

    def __init__(self, parent=None,x = 0,y = 0):
        super().__init__(parent)

        self.ui = Ui_Register()
        self.background = QLabel(self)

        self.ui.setupUi(self)
        self.ui.regist.clicked.connect(self.add)
        self.ui.cancel.clicked.connect(self.reject)

        self.background.setPixmap(QPixmap(":/background/resource/blue.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0,0,self.width(),self.height())
        self.background.lower()

        self.setWindowTitle("Register")
        self.setFixedSize(self.size())
        self.move(x,y)
        self.regist = False
        self.createVerification_code()
        
    def add(self):
        if self.ui.plot.text().upper() != self.random_str:
            return
        if self.ui.username.text() == "" or self.ui.password.text() == "":
            return
        with Mysql.connect() as db:
            with db.cursor() as cur:
                cur.execute("INSERT INTO login VALUES ('%s','%s')" % self.returnU_P())
        self.regist = True
        self.accept()

    def isRegist(self):
        return self.regist

    def returnU_P(self):
        return (self.ui.username.text(),self.ui.password.text())
    
    def createVerification_code(self):
        characters=string.digits+string.ascii_uppercase
        width,height,n_len,n_class=self.ui.verification_code.width(),self.ui.verification_code.height()-10,4,len(characters)
        generator=ImageCaptcha(width=width,height=height,font_sizes=[20])
        self.random_str=''.join([random.choice(characters) for j in range(4)])
        img=generator.generate_image(self.random_str)
        self.ui.verification_code.setPixmap(QPixmap.fromImage(pil_image_to_qimage(img)))
        #self.ui.verification_code.setScaledContents(True)