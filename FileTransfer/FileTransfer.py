from PySide2.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide2.QtGui import (QFont, QIcon)
from PySide2.QtWidgets import *

import os
import sys
import socket
from datetime import datetime
import threading
import shutil

import resourches

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(742, 577)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.994, stop:0 rgba(20, 21, 22, 255), stop:1 rgba(54, 64, 80, 255));\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.host_frame = QFrame(self.content_frame)
        self.host_frame.setObjectName(u"host_frame")
        self.host_frame.setMinimumSize(QSize(0, 140))
        self.host_frame.setMaximumSize(QSize(16777215, 200))
        self.host_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.host_frame.setFrameShape(QFrame.StyledPanel)
        self.host_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.host_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(70, 0, 179, 0)
        self.file_radio = QRadioButton(self.host_frame)
        self.file_radio.setObjectName(u"file_radio")
        self.file_radio.setMaximumSize(QSize(16777215, 32))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.file_radio.setFont(font)
        self.file_radio.setStyleSheet(u"QRadioButton#file_radio{\n"
"\n"
"	color: rgb(185, 185, 185);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"\n"
"\n"
"}\n"
"\n"
"QRadioButton#file_radio::indicator::unchecked:hover {\n"
"	image: url(:/resurssit/icons/4081326461553668576-32.png);\n"
"	margin-top:1px;\n"
"	margin-left:1px;\n"
"	width: 31px;\n"
"    height: 31px;\n"
"}\n"
"QRadioButton#file_radio::indicator::checked:hover {\n"
"    image: url(:/resurssit/icons/4081326461553668576-32.png);\n"
"	margin-top:1px;\n"
"	margin-left:1px;\n"
"	width: 31px;\n"
"    height: 31px;\n"
"}\n"
"\n"
"QRadioButton#file_radio::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"\n"
"}\n"
"QRadioButton#file_radio::indicator::unchecked {	\n"
"	image: url(:/resurssit/icons/4081326461553668576-32.png);\n"
"}\n"
"QRadioButton#file_radio::indicator::checked {	\n"
"	image: url(:/resurssit/icons/4081326461553668576-32.png);\n"
"color: rgb(185, 185, 185);\n"
"}")

        self.horizontalLayout_3.addWidget(self.file_radio)

        self.send_radio = QRadioButton(self.host_frame)
        self.send_radio.setObjectName(u"send_radio")
        self.send_radio.setFont(font)
        self.send_radio.setStyleSheet(u"QRadioButton#send_radio{\n"
"\n"
"	color: rgb(185, 185, 185);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"\n"
"QRadioButton#send_radio::indicator::unchecked:hover {\n"
"	\n"
"	image: url(:/resurssit/icons/15731092601553668592-32.png);\n"
"	margin-top:1px;\n"
"	margin-left:1px;\n"
"	width: 32px;\n"
"    height: 32px;\n"
"}\n"
"QRadioButton#send_radio::indicator::checked:hover {\n"
"   image: url(:/resurssit/icons/15731092601553668592-32.png);\n"
"	margin-top:1px;\n"
"	margin-left:1px;\n"
"	width: 32px;\n"
"    height: 32px;\n"
"}\n"
"\n"
"QRadioButton#send_radio::indicator {\n"
"    width: 31px;\n"
"    height: 31px;\n"
"\n"
"}\n"
"QRadioButton#send_radio::indicator::unchecked {	\n"
"	image: url(:/resurssit/icons/15731092601553668592-32.png);\n"
"}\n"
"QRadioButton#send_radio::indicator::checked {	\n"
"	image: url(:/resurssit/icons/15731092601553668592-32.png);\n"
"color: rgb(185, 185, 185);\n"
"}")

        self.horizontalLayout_3.addWidget(self.send_radio)


        self.verticalLayout_2.addWidget(self.host_frame)

        self.client_frame = QFrame(self.content_frame)
        self.client_frame.setObjectName(u"client_frame")
        self.client_frame.setMinimumSize(QSize(0, 140))
        self.client_frame.setMaximumSize(QSize(16777215, 100))
        self.client_frame.setStyleSheet(u"QFrame{\n"
"border-top: 1px solid rgb(48, 53, 61);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}")
        self.client_frame.setFrameShape(QFrame.StyledPanel)
        self.client_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.client_frame)
        self.horizontalLayout_2.setSpacing(32)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(70, 0, 0, 0)
        self.path_radio = QRadioButton(self.client_frame)
        self.path_radio.setObjectName(u"path_radio")
        self.path_radio.setFont(font)
        self.path_radio.setStyleSheet(u"QRadioButton#path_radio{\n"
"\n"
"	color: rgb(185, 185, 185);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"\n"
"QRadioButton#path_radio::indicator::unchecked:hover {\n"
"	\n"
"	image: url(:/resurssit/icons/6120438951553668577-32.png);\n"
"	margin-top:1px;\n"
"	margin-left:1px;\n"
"	width: 32px;\n"
"    height: 32px;\n"
"\n"
"	\n"
"}\n"
"QRadioButton#path_radio::indicator::checked:hover {\n"
"    image: url(:/resurssit/icons/6120438951553668577-32.png);\n"
"	margin-top:1px;\n"
"	margin-left:1px;\n"
"	width: 32px;\n"
"    height: 32px;\n"
"\n"
"}\n"
"\n"
"QRadioButton#path_radio::indicator {\n"
"    width: 31px;\n"
"    height: 31px;\n"
"\n"
"}\n"
"QRadioButton#path_radio::indicator::unchecked {	\n"
"	image: url(:/resurssit/icons/6120438951553668577-32.png);\n"
"}\n"
"QRadioButton#path_radio::indicator::checked {	\n"
"	image: url(:/resurssit/icons/6120438951553668577-32.png);\n"
"color: rgb(185, 185, 185);\n"
"}")

        self.horizontalLayout_2.addWidget(self.path_radio)

        self.lineEdit = QLineEdit(self.client_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(180, 16777215))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setMinimumWidth(180)
        self.lineEdit.setStyleSheet(u"background-color: rgb(42, 49, 59);\n"
"border: 0px solid;\n"
"color: rgb(185, 185, 185);")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.receive_radio = QRadioButton(self.client_frame)
        self.receive_radio.setObjectName(u"receive_radio")
        self.receive_radio.setFont(font)
        self.receive_radio.setMinimumWidth(200)
        self.receive_radio.setStyleSheet(u"QRadioButton#receive_radio{\n"
"\n"
"	color: rgb(185, 185, 185);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	padding-bottom: 5px;\n"
"\n"
"}\n"
"\n"
"QRadioButton#receive_radio::indicator::unchecked:hover {\n"
"	image: url(:/resurssit/icons/18874797511553668575-32.png);\n"
"	margin-top:1px;\n"
"	margin-left:1px;\n"
"	width: 32px;\n"
"    height: 32px;\n"
"}\n"
"QRadioButton#receive_radio::indicator::checked:hover {\n"
"    image: url(:/resurssit/icons/18874797511553668575-32.png);\n"
"	margin-top:1px;\n"
"	margin-left:1px;\n"
"	width: 32px;\n"
"    height: 32px;\n"
"}\n"
"\n"
"QRadioButton#receive_radio::indicator {\n"
"    width: 31px;\n"
"    height: 31px;\n"
"\n"
"}\n"
"QRadioButton#receive_radio::indicator::unchecked {	\n"
"	image: url(:/resurssit/icons/18874797511553668575-32.png);\n"
"}\n"
"QRadioButton#receive_radio::indicator::checked {	\n"
"	image: url(:/resurssit/icons/18874797511553668575-32.png);\n"
"color: rgb(185, 185, 185);\n"
"}")

        self.horizontalLayout_2.addWidget(self.receive_radio)


        self.verticalLayout_2.addWidget(self.client_frame)

        self.frame_3 = QFrame(self.content_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setMaximumSize(QSize(16777215, 300))
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 140, 0, 0)
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.progressBar.setFont(font2)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid rgb(38, 45, 56);\n"
"    border-radius: 5px;\n"
"	color: rgb(185, 185, 185);\n"
"    \n"
"	\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"   \n"
"	\n"
"	\n"
"	background-color: rgb(57, 67, 83);\n"
"    width: 1px;\n"
"}\n"
"\n"
"QProgressBar:text {\n"
"	color: rgb(148, 230, 255);\n"
"}\n"
"   ")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(100)
        self.progressBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(25, 23, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.content_frame)

        self.terminal_frame = QFrame(self.frame)
        self.terminal_frame.setObjectName(u"terminal_frame")
        self.terminal_frame.setMinimumSize(QSize(0, 100))
        self.terminal_frame.setMaximumSize(QSize(16777215, 100))
        self.terminal_frame.setStyleSheet(u"QFrame#terminal_frame{\n"
"background-color: rgba(122, 122, 122, 30);\n"
"color: rgb(185, 185, 185);\n"
"border-top: 1px solid rgb(23, 26, 33);\n"
"}")
        self.terminal_frame.setFrameShape(QFrame.StyledPanel)
        self.terminal_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.terminal_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.listWidget = QListWidget(self.terminal_frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 80))
        self.listWidget.setStyleSheet(u"QListWidget#listWidget{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 0px solid;\n"
"color: rgb(185, 185, 185);\n"
"}\n"
"\n"
"QScrollBar\n"
"{\n"
"background : rgb(179, 179, 179);\n"
"width: 6px;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background :rgb(70, 80, 95);\n"
"\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"     background: rgb(55, 62, 75);\n"
"	 height: 0px;\n"
"	 width: 0px;\n"
" }\n"
"\n"
"")     
        self.scroll_bar = QScrollBar(self.terminal_frame)
        self.scroll_bar.setStyleSheet("QScrollBar{\n"
"background : rgb(179, 179, 179);\n"
"width: 6px;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background :rgb(70, 80, 95);\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
     "background: rgb(55, 62, 75);\n"
	 "height: 0px;\n"
	 "width: 0px;\n"
 "}\n"
)
        self.listWidget.setVerticalScrollBar(self.scroll_bar)
        
        self.scroll_bar2 = QScrollBar(self.terminal_frame)
        self.scroll_bar2.setStyleSheet("QScrollBar{\n"
"background : rgb(179, 179, 179);\n"
"width: 6px;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background :rgb(70, 80, 95);\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
     "background: rgb(55, 62, 75);\n"
	 "height: 0px;\n"
	 "width: 0px;\n"
 "}\n"
)       
        self.listWidget.setHorizontalScrollBar(self.scroll_bar2)

        self.verticalLayout_3.addWidget(self.listWidget)


        self.verticalLayout.addWidget(self.terminal_frame)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FileTransfer", None))
        self.file_radio.setText(QCoreApplication.translate("MainWindow", u" Select files", None))
        self.send_radio.setText(QCoreApplication.translate("MainWindow", u" Send files", None))
        self.path_radio.setText(QCoreApplication.translate("MainWindow", u" Select download path", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Host ip address", None))
        self.receive_radio.setText(QCoreApplication.translate("MainWindow", u" Receive files", None))
    # retranslateUi

        Form.setWindowIcon(QIcon(r':\resurssit\icons\8722222091536837273_48_WTc_icon.ico'))

        self.font = QFont()
        self.font.setFamily(u"Segoe UI")
        self.font.setPointSize(10)

        # get saved host IP address

        with open('host.txt', "r") as f:
                lines = f.readlines()
                global ip
                if not lines:
                        self.lineEdit.setText("Host ip address")     
                else:
                        ip = lines[0].strip("[]'")
                        self.lineEdit.setText(ip)
                f.close()

        self.progressBar.setValue(0)
  
###############################################################################################################################################################################
# Buttons
##############################################################################################################################################################################

        self.file_radio.clicked.connect(self.getfile)
        self.send_radio.clicked.connect(self.host)
        self.receive_radio.clicked.connect(self.client)
        self.path_radio.clicked.connect(self.getDirectory)
        self.lineEdit.textChanged.connect(self.ip_address)

        

########################################################################################################################################################################################################################################

    # select files to send and append them to list

    def getfile(self): 
        global fileName
        global current_time
        global files_list
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileNames()
        files_list = []
        index = 0
        for i in fileName:
                files_list.append(os.path.basename(fileName[index]))
                index += 1

        index = 0
        for i in files_list:
                self.getTime()
                item = QListWidgetItem("[" + current_time + "] - Selected " + files_list[index])
                item.setFont(self.font)
                self.listWidget.addItem(item)
                self.listWidget.scrollToItem(item)
                self.listWidget.scrollToItem(item)
                index += 1
        return fileName

    def host(self):
        global current_time
        global files_list

        # Check if user has selected any files

        try:

                if not files_list:
                        self.getTime()

                        item = QListWidgetItem("[" + current_time + "] - Error | No files selected" )
                        item.setFont(self.font)
                        item.setTextColor("red")
                        self.listWidget.addItem(item)
                        self.listWidget.scrollToItem(item)
                        self.listWidget.scrollToItem(item)
                        return
        except:
                item = QListWidgetItem("[" + current_time + "] - Error | No files selected" )
                item.setFont(self.font)
                item.setTextColor("red")
                self.listWidget.addItem(item)
                self.listWidget.scrollToItem(item)
                self.listWidget.scrollToItem(item)
                return

        # Wait for client and start another thread for sending files

        self.getTime()
        item = QListWidgetItem("[" + current_time + "] - Waiting for client to accept transfer..." )
        item.setFont(self.font)
        self.listWidget.addItem(item)
        self.listWidget.scrollToItem(item)
        
        
        thread = threading.Thread(target=self.host2, args=(), kwargs={})
        thread.start()

    def host2(self):
        global fileName
        global files_list

        host = ""
        port = 9999

        # Send file names list to client

        s = socket.socket()
        s.bind((host,port))
        s.listen(1)
        conn, addr = s.accept()

        data = str(files_list)
        print(files_list)
        data = data.encode()
        conn.send(data)
        conn.close()
        s.close()

        # Send file size list to client

        s = socket.socket()
        s.bind((host,port))
        s.listen(1)
        conn, addr = s.accept()
        
        file_size = []
        index = 0
        for i in fileName:
                size = os.path.getsize(fileName[index])
                file_size.append(size)
                index += 1

        file_size = str(file_size)
        file_size = file_size.encode()
        conn.send(file_size)

        conn.close()
        s.close()
        
        # Send files invidually, create new socket in each loop and wait for client to accept before sending next file

        index = 0
        for i in fileName:
                fileName[0] = fileName[0].strip("[]''")
                
                s = socket.socket()
                s.bind((host,port))
                s.listen(1)
                conn, addr = s.accept()

                file = open(fileName[index], "rb")
                file_data = file.read()
                conn.send(file_data)
                conn.close()
                s.close()
                file.close()

                index += 1


        # Update terminal

        self.getTime()
        item = QListWidgetItem("[" + current_time + "] - Data has been transmitted succesfully" )
        item.setFont(self.font)
        self.listWidget.addItem(item)
        self.listWidget.scrollToItem(item)


    def client(self): 
        global current_time
        global response
        global ip

        # Check if user has set IP address

        try:
                host = str(ip)
                port = 9999
        except:
                self.getTime()
                item = QListWidgetItem("[" + current_time + "] - Error | Invalid IP Address" )
                item.setFont(self.font)
                item.setTextColor("red")
                self.listWidget.addItem(item)
                self.listWidget.scrollToItem(item)
                return


        # Receive file_names list and file_size list
        try:
                s = socket.socket()
                s.settimeout(3)
                s.connect((host,port))
                s.settimeout(None)

                # File names list
                name_data = s.recv(40960)
                name_data = name_data.decode()
                name_data = eval(name_data)
                s.close()

                s = socket.socket()
                s.settimeout(3)
                s.connect((host,port))
                s.settimeout(None)

                # File size list
                file_size = s.recv(40960)
                file_size = file_size.decode()
                file_size = eval(file_size)
                s.close()

                # Go trough name_data list, create new file and receive data, each loop creates a new socket and closes it
        
                index = 0

                for i in name_data:
                        s = socket.socket()
                        s.connect((host,port))

                        # Set default download location
                        current_location = os.path.realpath(
                        os.path.join(os.getcwd(), os.path.dirname(__file__)))

                        file_path = os.path.join(current_location, "downloads")
                        file_path = os.path.join(file_path, str(name_data[index]))

                        # Update terminal
                        self.getTime()
                        item = QListWidgetItem("[" + current_time + "] - Downloading file " + "[" + str(index + 1) +"/"+ str(len(name_data)) + "]")
                        item.setFont(self.font)
                        self.listWidget.addItem(item)
                        self.listWidget.scrollToItem(item)

                
                        # Set progress bar max value as file size in bytes
                        size = file_size[index]
                        self.progressBar.setRange(0,size)
                        downloaded = 0

                        # Create file and write data
                        file = open(file_path, "wb")
                        while True:
                                file_data = s.recv(4096)
                                if not file_data:
                                        self.progressBar.setValue(size)
                                        break
                                file.write(file_data)

                                # Update progress bar
                                downloaded += len(file_data)
                                self.progressBar.setValue(downloaded)
                                app.processEvents()
                                    
                        file.close()
                        s.close()         
                                        
                        try:
                                # Test if user has set path folder, if true copy files to path location and delete them from downloads folder

                                print(response)

                                toremove = name_data[index]
                                target = r''+response+''
                                shutil.copyfile(file_path, os.path.join(target, toremove))
                                os.remove(file_path)
                                        
                        except:
                                        pass

                                                     
                        index += 1  
                      
                        

        except:
                self.getTime()
                item = QListWidgetItem("[" + current_time + "] - Error | Connection failed" )
                item.setFont(self.font)
                item.setTextColor("red")
                self.listWidget.addItem(item)
                self.listWidget.scrollToItem(item)
                return
        
        # Update terminal

        self.getTime()
        item = QListWidgetItem("[" + current_time + "] - Download complete" )
        item.setFont(self.font)
        self.listWidget.addItem(item)
        self.listWidget.scrollToItem(item)
        
    def getTime(self):
        global current_time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

    def getDirectory(self):
        global response
        # Open file browser
        response = QFileDialog.getExistingDirectory()
        
        # Check if user chose anything
        if response == "":
                return

        # Update terminal
        self.getTime()
        item = QListWidgetItem("[" + current_time + "] - Path set to: " + response )
        item.setFont(self.font)
        self.listWidget.addItem(item)
        self.listWidget.scrollToItem(item)

        return response 

    def ip_address(self):
             # Save ip address to file
             global ip
             ip = self.lineEdit.text()
             f = open("host.txt","w")
             f.write(ip)
             f.close()


if __name__ == "__main__":
        app = QApplication(sys.argv)
        Form = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())    
