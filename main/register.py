from PySide6.QtWidgets import QDialog, QLabel, QMessageBox
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Slot
from ui.ui_register import Ui_Register
from func.mysql import Mysql
from captcha.image import ImageCaptcha
import rc_resource
import numpy as np 
import random, string
def has_punctuation(s):
    pattern = re.compile(r'[^\w\s]')
    return bool(pattern.search(s))
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
    def __init__(self, parent=None,x = 0,y = 0,module = "register"):
        super().__init__(parent)

        self.ui = Ui_Register()
        self.background = QLabel(self)

        self.ui.setupUi(self)

        self.background.setPixmap(QPixmap(":/background/resource/blue.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0,0,self.width(),self.height())
        self.background.lower()

        self.setFixedSize(self.size())
        self.move(x,y)
        self.regist = False
        self.createVerification_code()
        if module == "register":
            self.setWindowTitle("注册")
            self.ui.regist.clicked.connect(self.add)
        else:
            self.ui.tip1.setText("原密码")
            self.setWindowTitle("修改密码")
            self.ui.regist.clicked.connect(self.changePassword)
            self.ui.regist.setText("确认")
        self.ui.cancel.clicked.connect(self.reject)

    def setUsername(self,username):
        self.username = username

    def add(self):
        message =  QMessageBox()
        if len(self.ui.username.text()) not in range(1,15):
            message.setIcon(QMessageBox.Critical)
            message.setText("用户名长度应在1-15之间")
            message.exec()
            return
        if has_punctuation(self.ui.username.text()):
            message.setIcon(QMessageBox.Critical)
            message.setText("用户名不能包含特殊字符")
            message.exec()
            return
        if len(self.ui.password.text()) not in range(6,15):
            message.setIcon(QMessageBox.Critical)
            message.setText("密码长度应在6-15之间")
            message.exec()
            return
        if self.ui.password_2.text() != self.ui.password.text():
            message.setIcon(QMessageBox.Critical)
            message.setText("二次密码不一致")
            message.exec()
            return
        if self.ui.plot.text().upper() != self.random_str:
            message.setIcon(QMessageBox.Critical)
            message.setText("验证码错误")
            message.exec()
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

    @Slot()
    def changePassword(self):
        message =  QMessageBox()
        if self.ui.password.text() != self.ui.password_2.text():
            message.setIcon(QMessageBox.Critical)
            message.setText("二次密码不一致")
            message.exec()
            return
        if self.ui.plot.text().upper() != self.random_str:
            message.setIcon(QMessageBox.Critical)
            message.setText("验证码错误")
            message.exec()
        else:
            try:
                Mysql.execute(Mysql.connect(),"update login set password = '%s' where username = '%s' and password = '%s';" % (self.ui.password.text(),self.username,self.ui.username.text()))
            except:
                message.setIcon(QMessageBox.Critical)
                message.setText("原密码不正确")
                message.exec()
            message.setIcon(QMessageBox.Information)
            message.setText("修改成功")
            message.exec()
            self.close()
    def mousePressEvent(self, event):
        if self.ui.verification_code.underMouse():
            self.createVerification_code()
        return super().mousePressEvent(event)