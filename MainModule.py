from PIL import Image, ImageDraw, ImageFont
import qrcode
import random
import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from qtpy import QtCore, QtGui

filename = None

def onClick():
    try:
        print('Clicked !')

        image = Image.new('RGB', (1000, 900), (255, 255, 255))
        tempimg = Image.open('idback.jpg')

        width = 1060
        height = 960
        tempidback = tempimg.resize((width, height), Image.NEAREST)
        tempidback.save('tempidback.jpg')
        tempidback = Image.open('tempidback.jpg')

        image.paste(tempidback)
        draw = ImageDraw.Draw(image)



        os.system('title ID Card Generator by Harshit')

        # Starting Position of the message
        print('\n\nAll fields are Mandatory')
        print('Avoid any kind of Spelling Mistakes')
        print('Write everything in Uppercase letters')

        (x, y) = (50, 50)
        message = str(dlg.companyName.text())
        print(message)
        company = message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=80)
        draw.text((x, y), message, fill=color, font=font)

        # adding an unique id number
        (x, y) = (600, 75)
        idno = random.randint(10000000, 90000000)
        message = str('ID' + str(idno))
        print(message)
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=60)
        draw.text((x, y), message, fill=color, font=font)

        # adding name
        (x, y) = (50, 250)
        message = str(dlg.username.text())
        print(message)
        name = message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), 'Name : ' + message, fill=color, font=font)

        # adding Gender and Age
        (x, y) = (50, 350)
        message = str(dlg.gender.text())
        print(message)
        color = 'rgb(0, 0, 0)'
        draw.text((x, y), 'Gender : ' + message, fill=color, font=font)

        # (x, y) = (250, 350)
        # message = str(dlg.age.text())
        # print(message)
        # color = 'rgb(0, 0, 0)'
        # draw.text((x, y), 'Age : ' + message, fill=color, font=font)

        (x, y) = (50, 450)
        message = str(dlg.dob.text())
        print(message)
        color = 'rgb(0, 0, 0)'
        draw.text((x, y), 'DOB : ' + message, fill=color, font=font)

        # adding blood group
        (x, y) = (50, 550)
        message = str(dlg.blood.text())
        print(message)
        color = 'rgb(255, 0, 0)'
        draw.text((x, y), 'Blood Group : ' + message, fill=color, font=font)

        # adding phone number
        (x, y) = (50, 650)
        message = str(dlg.number.text())
        print(message)
        color = 'rgb(0, 0, 0)'
        draw.text((x, y), 'Phone No. : ' + message, fill=color, font=font)

        # adding address
        (x, y) = (50, 750)
        message = str(dlg.address.text())
        print(message)
        color = 'rgb(0, 0, 0)'
        draw.text((x, y), 'Address : ' + message, fill=color, font=font)

        # Save the edited image
        image.save(name + '.png')

        # Adding QR Code

        img = qrcode.make(str(company) + '\n' + str(idno) + '\n' + str(name))
        img.save(str(idno) + '.bmp')

        til = Image.open(name + '.png')
        im = Image.open(str(idno) + '.bmp')
        profile = Image.open(filename)
        width = 250
        height = 250
        im2 = profile.resize((width, height), Image.NEAREST)
        barcode = im.resize((width, height), Image.NEAREST)
        im2.save('passport.jpg')
        barcode.save('barcode.jpg')
        profile = Image.open('passport.jpg')
        im = Image.open('barcode.jpg')
        til.paste(profile, (650, 250))
        til.paste(im, (650, 520))
        til.save(name + '.png')


        # img = cv2.imread(name + '.png')
        # color = [0, 0, 0]  # 'cause purple!
        # # border widths; I set them all to 150
        # top, bottom, left, right = [30] * 4
        # img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
        # lineThickness = 2
        # cv2.line(img_with_border, (0, 220), (1060, 220), (0, 0, 0), lineThickness)
        # cv2.imwrite(name + '.png', img_with_border)

        label = dlg2.image
        pixmap = QPixmap(name + '.png')
        pixmap = pixmap.scaled(pixmap.width() / 1.5, pixmap.height() / 1.5)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        dlg2.resize(pixmap.width(), pixmap.height())
        dlg2.show()
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Fill All Necessary Details !')
        msg.setWindowTitle("Error")
        msg.exec_()

def browseImg():
    global filename
    filename, _ = QFileDialog.getOpenFileName(dlg, 'Single File', QtCore.QDir.rootPath(), '*.jpg *.png')
    dlg.imgtext.setText(filename)

app = QApplication([])
dlg = loadUi('ui.ui')
dlg2 = loadUi('ui2.ui')
dlg.pushButton.clicked.connect(onClick)
dlg.browse.clicked.connect(browseImg)

label = dlg.image
pixmap = QPixmap('testimg.jpg')
pixmap = pixmap.scaled(pixmap.width()/2, pixmap.height()/1.9)
label.setPixmap(pixmap)
label.resize(pixmap.width(), pixmap.height())
dlg.resize(pixmap.width(), pixmap.height())

test = dlg.head
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

test = dlg.label_1
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

test = dlg.label_2
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

test = dlg.label_3
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

test = dlg.label_4
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

test = dlg.label_5
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

test = dlg.label_6
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

test = dlg.label_7
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

test = dlg.label_8
pal = test.palette()
pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
test.setPalette(pal)

dlg.companyName.setPlaceholderText("Enter Company Name")
dlg.username.setPlaceholderText("Enter Full Name")
dlg.gender.setPlaceholderText("Enter Your Gender")
dlg.dob.setPlaceholderText("Enter Your Date of Birth")
dlg.age.setPlaceholderText("Enter Your Age")
dlg.blood.setPlaceholderText("Enter Your Blood Group")
dlg.number.setPlaceholderText("Enter Your Mobile Number")
dlg.address.setPlaceholderText("Enter Your Address")


dlg.setAttribute(QtCore.Qt.WA_DeleteOnClose)
dlg.setWindowFlags(dlg.windowFlags() |
                              QtCore.Qt.WindowSystemMenuHint |
                              QtCore.Qt.WindowMinMaxButtonsHint)


dlg.show()
app.exec()

