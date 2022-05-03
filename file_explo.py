from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import QKeySequence, QCursor, QDesktopServices
import os, shutil


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 896)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.leftPane = QtWidgets.QTreeView(self.centralwidget)
        self.leftPane.setGeometry(QtCore.QRect(10, 180, 301, 651))
        self.leftPane.setObjectName("leftPane")
        
        self.mainArea = QtWidgets.QTableView(self.centralwidget)
        self.mainArea.setGeometry(QtCore.QRect(320, 180, 781, 651))
        self.mainArea.setObjectName("mainArea")
        self.mainArea.setShowGrid(False)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1091, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background: white;")
        
        self.dark_Button = QtWidgets.QToolButton(self.frame)
        self.dark_Button.setGeometry(QtCore.QRect(10, 120, 51, 41))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons8-moon-and-stars-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dark_Button.setIcon(icon8)
        self.dark_Button.setIconSize(QtCore.QSize(50, 50))
        self.dark_Button.setObjectName("darkButton")
        self.dark_Button.setStyleSheet("border: none;")
        self.dark_Button.clicked.connect(self.darkMode)

        self.back_button = QtWidgets.QToolButton(self.frame)
        self.back_button.setGeometry(QtCore.QRect(70, 120, 51, 41))
        self.back_button.setStyleSheet("border: none;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-arrow-pointing-left-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QtCore.QSize(30, 30))
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.go_back)       
        
        self.next_button = QtWidgets.QToolButton(self.frame)
        self.next_button.setGeometry(QtCore.QRect(120, 120, 51, 41))
        self.next_button.setStyleSheet("border: none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons8-arrow-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon1)
        self.next_button.setIconSize(QtCore.QSize(30, 30))
        self.next_button.setObjectName("next_button")
        self.next_button.clicked.connect(self.go_next)

        self.prev_button = QtWidgets.QToolButton(self.frame)
        self.prev_button.setGeometry(QtCore.QRect(180, 120, 51, 41))
        self.prev_button.setStyleSheet("border: none;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons8-send-letter-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev_button.setIcon(icon2)
        self.prev_button.setIconSize(QtCore.QSize(40, 40))
        self.prev_button.setObjectName("prev_button")
        self.prev_button.clicked.connect(self.move_prev)
        
        self.path_label = QtWidgets.QLabel(self.frame)
        self.path_label.setGeometry(QtCore.QRect(260, 127, 47, 31))
        self.path_label.setStyleSheet("font-size: 15px; font-family: Bahnschrift SemiBold;")
        self.path_label.setObjectName("path_label")  

        self.path = QtWidgets.QTextBrowser(self.frame)
        self.path.setGeometry(QtCore.QRect(310, 130, 781, 31))
        self.path.setObjectName("path")
        
        self.newFolder_button = QtWidgets.QToolButton(self.frame)
        self.newFolder_button.setGeometry(QtCore.QRect(20, 0, 91, 81))
        self.newFolder_button.setStyleSheet("border: none;")
        self.newFolder_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons8-folder-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newFolder_button.setIcon(icon3)
        self.newFolder_button.setIconSize(QtCore.QSize(60, 60))
        self.newFolder_button.setObjectName("newFolder_button")
        self.newFolder_button.clicked.connect(self.newFolder)
        
        self.newFolder_label = QtWidgets.QLabel(self.frame)
        self.newFolder_label.setGeometry(QtCore.QRect(26, 80, 81, 21))
        self.newFolder_label.setStyleSheet("font-size: 15px; font-family: forte;")
        self.newFolder_label.setObjectName("newFolder_label")
        
        self.delete_button = QtWidgets.QToolButton(self.frame)
        self.delete_button.setGeometry(QtCore.QRect(130, 0, 101, 91))
        self.delete_button.setStyleSheet("border: none;")
        self.delete_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons8-full-recycle-bin-240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon4)
        self.delete_button.setIconSize(QtCore.QSize(60, 60))
        self.delete_button.setObjectName("delete_button")
        self.delete_button.clicked.connect(self.deleteFileFolder)

        self.cut_button = QtWidgets.QToolButton(self.frame)
        self.cut_button.setGeometry(QtCore.QRect(230, 0, 101, 91))
        self.cut_button.setStyleSheet("border: none;")
        self.cut_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons8-cut-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cut_button.setIcon(icon5)
        self.cut_button.setIconSize(QtCore.QSize(60, 60))
        self.cut_button.setObjectName("cut_button")
        self.cut_button.clicked.connect(self.cut)
        
        self.copy_button = QtWidgets.QToolButton(self.frame)
        self.copy_button.setGeometry(QtCore.QRect(330, 0, 111, 101))
        self.copy_button.setStyleSheet("border: none;")
        self.copy_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons8-copy-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_button.setIcon(icon6)
        self.copy_button.setIconSize(QtCore.QSize(60, 60))
        self.copy_button.setObjectName("copy_button")
        self.copy_button.clicked.connect(self.copy)
        
        self.paste_button = QtWidgets.QToolButton(self.frame)
        self.paste_button.setGeometry(QtCore.QRect(440, 0, 101, 91))
        self.paste_button.setStyleSheet("border: none;")
        self.paste_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons8-paste-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paste_button.setIcon(icon7)
        self.paste_button.setIconSize(QtCore.QSize(60, 60))
        self.paste_button.setObjectName("paste_button")
        self.paste_button.clicked.connect(self.paste)
        
        self.delete_label = QtWidgets.QLabel(self.frame)
        self.delete_label.setGeometry(QtCore.QRect(160, 80, 51, 21))
        self.delete_label.setStyleSheet("font-size: 15px; font-family: forte;")
        self.delete_label.setObjectName("delete_label")

        self.cut_label = QtWidgets.QLabel(self.frame)
        self.cut_label.setGeometry(QtCore.QRect(270, 80, 31, 21))
        self.cut_label.setStyleSheet("font-size: 15px; font-family: forte;")
        self.cut_label.setObjectName("cut_label")
        
        self.copy_label = QtWidgets.QLabel(self.frame)
        self.copy_label.setGeometry(QtCore.QRect(360, 80, 51, 21))
        self.copy_label.setStyleSheet("font-size: 15px; font-family: forte;")
        self.copy_label.setObjectName("copy_label")
        
        self.paste_label = QtWidgets.QLabel(self.frame)
        self.paste_label.setGeometry(QtCore.QRect(470, 80, 51, 21))
        self.paste_label.setStyleSheet("font-size: 15px; font-family: forte;")
        self.paste_label.setObjectName("paste_label")
        
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(120, 20, 16, 71))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(220, 20, 16, 71))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(320, 20, 16, 71))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(430, 20, 16, 71))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        
        self.bottom_view = QtWidgets.QTextBrowser(self.centralwidget)
        self.bottom_view.setGeometry(QtCore.QRect(10, 840, 1091, 31))
        self.bottom_view.setObjectName("bottom_view")
        MainWindow.setCentralWidget(self.centralwidget)
        self.bottom_view.setText("Developed by AKASH KUMAR SINGH")
        self.bottom_view.setStyleSheet("font-size: 15px; font-family: Lucida Calligraphy; color: red;")
        self.bottom_view.setAlignment(Qt.AlignCenter)
        self.bottom_view.verticalScrollBar().hide()

        self.hideButton = QtWidgets.QPushButton(self.centralwidget)
        self.hideButton.setGeometry(QtCore.QRect(1010, 850, 61, 20))
        self.hideButton.setObjectName("hideButton")
        self.hideButton.setStyleSheet("border: none; background: white")
        self.hideButton.clicked.connect(self.enableHidden)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actions()
        self.mainArea.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.mainArea.customContextMenuRequested.connect(self.context_menu)
        self.function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("File Manager", "File Manager"))
        self.back_button.setText(_translate("MainWindow", "..."))
        self.next_button.setText(_translate("MainWindow", "..."))
        self.path_label.setText(_translate("MainWindow", "Path"))
        self.prev_button.setText(_translate("MainWindow", "..."))
        self.newFolder_label.setText(_translate("MainWindow", "New Folder"))
        self.delete_label.setText(_translate("MainWindow", "Delete"))
        self.cut_label.setText(_translate("MainWindow", "Cut"))
        self.copy_label.setText(_translate("MainWindow", "Copy"))
        self.paste_label.setText(_translate("MainWindow", "Paste"))


    def function(self):
        self.mainModel = QDirModel()
        self.mainModel.setReadOnly(True)
        self.mainModel.setSorting(QDir.DirsFirst | QDir.IgnoreCase | QDir.Name)
        self.mainArea.setModel(self.mainModel)
        self.mainArea.setColumnWidth(0, 300)
        self.mainArea.verticalHeader().hide()

        self.dirModel = QFileSystemModel()
        self.dirModel.setReadOnly(True)
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Drives)
        self.leftPane.setModel(self.dirModel)
        self.leftPane.hideColumn(1)
        self.leftPane.hideColumn(2)
        self.leftPane.hideColumn(3)
        self.leftPane.setHeaderHidden(True)

        # Prequisites for move_back.
        self.prev_path = []
        self.curr = -1
        self.temp = ""
        self.cut_flag = False
        self.darkMode_flag = False
        self.hiddenEnabled = False

        self.leftPane.clicked.connect(self.left_to_main)
        self.mainArea.doubleClicked.connect(self.double_main)

    def path_left(self):
        self.index = self.leftPane.currentIndex()
        self.path_address = self.dirModel.filePath(self.index)
        try:
            if self.path_address != self.prev_path[self.curr]:
                self.prev_path.append(self.path_address)
                self.curr += 1
        except:
            self.prev_path.append(self.path_address)
            self.curr += 1

    def path_main(self):
        self.index = self.mainArea.currentIndex()
        self.path_address = self.mainModel.filePath(self.index)
        try:
            if os.path.isdir(self.path_address) and (self.path_address != self.prev_path[self.curr]):
                self.prev_path.append(self.path_address)
                self.curr += 1
        except:
            self.prev_path.append(self.path_address)
            self.curr += 1

    def left_to_main(self):
        self.path_left()
        self.prev_path.insert(self.curr + 1, self.prev_path[-1])
        self.prev_path = self.prev_path[:self.curr + 1]
        self.mainArea.setRootIndex(self.mainModel.index(self.path_address))
        self.mainArea.setSortingEnabled(True)
        self.path.setText(self.path_address.replace("/", "\\"))

    def double_main(self):
        self.path_main()
        self.prev_path.insert(self.curr, self.prev_path[-1])
        self.prev_path = self.prev_path[:self.curr + 1]
        if os.path.isdir(self.path_address):
            self.mainArea.setRootIndex(self.mainModel.index(self.path_address))
            self.path.setText(self.path_address.replace("/", "\\"))
            self.leftPane.setCurrentIndex(self.dirModel.index(self.path_address))
            self.leftPane.setFocus()
        else:
            os.startfile(self.path_address, "open")

    def actions(self):
        self.Open = QAction("Open", triggered = self.double_main)
        self.mainArea.addAction(self.Open)

        self.Create = QAction("New Folder", triggered = self.newFolder)
        self.Create.setShortcut(QKeySequence("Ctrl+n"))
        self.mainArea.addAction(self.Create)

        self.Cut = QAction("Cut", triggered = self.cut)
        self.Cut.setShortcut(QKeySequence("Ctrl+x"))
        self.mainArea.addAction(self.Cut)

        self.Copy = QAction("Copy", triggered = self.copy)
        self.Copy.setShortcut(QKeySequence("Ctrl+c"))
        self.mainArea.addAction(self.Copy)

        self.Paste = QAction("Paste", triggered = self.paste)
        self.Paste.setShortcut(QKeySequence("Ctrl+v"))
        self.mainArea.addAction(self.Paste)

        self.Rename = QAction("Rename", triggered = self.rename)
        self.Rename.setShortcut(QKeySequence(Qt.Key_F2))
        self.mainArea.addAction(self.Rename)

        self.Delete = QAction("Delete", triggered = self.deleteFileFolder)
        self.Delete.setShortcut(QKeySequence("Del"))
        self.mainArea.addAction(self.Delete)


    def context_menu(self):
        menu = QMenu(self.mainArea)
        menu.addAction(self.Open)
        menu.addAction(self.Create)
        menu.addAction(self.Rename)
        menu.addAction(self.Cut)
        menu.addAction(self.Copy)
        menu.addAction(self.Paste)
        menu.addAction(self.Delete)

        cursor = QCursor()
        menu.exec_(cursor.pos())

    def refresh_mainArea(self):
        self.mainModel.refresh(self.index)
        self.mainArea.setRootIndex(self.mainModel.index(self.path_address))


    def newFolder(self):
        self.path_left()
        dlg = QInputDialog(self.mainArea)
        foldername, ok = dlg.getText(self.mainArea, 'Folder Name', "Folder Name:", QLineEdit.Normal, "", Qt.Dialog)
        if ok:
            success = QDir(self.path_address).mkdir(foldername)
            self.refresh_mainArea()

    def deleteFileFolder(self):
        self.path_main()
        try:
            if os.path.isdir(self.path_address):
                shutil.rmtree(self.path_address, ignore_errors = True)
            else:
                os.remove(self.path_address)
                self.refresh_mainArea()
        except:
            return

        self.path_left()
        self.refresh_mainArea()

    def move_prev(self):
        try:
            self.path_address = self.path_address[:(len(self.path_address) - len(os.path.basename(self.path_address)) - 1)]
        except:
            return
        self.mainArea.setRootIndex(self.mainModel.index(self.path_address))
        if self.path_address.isalpha():
            self.path.setText("")
            return
        self.path.setText(self.path_address)
        self.leftPane.setCurrentIndex(self.dirModel.index(self.path_address))
        self.leftPane.setFocus()

    def go_back(self):
        if self.curr <= 0:
            self.curr = 0
            return
        self.curr -= 1
        self.path_address = self.prev_path[self.curr]
        self.mainArea.setRootIndex(self.mainModel.index(self.path_address))
        self.path.setText(self.path_address.replace("/", "\\"))
        self.leftPane.setCurrentIndex(self.dirModel.index(self.path_address))
        self.leftPane.setFocus()

    def go_next(self):
        if self.curr >= len(self.prev_path) - 1:
            self.curr = len(self.prev_path) - 1
            return
        if self.curr < 0:
            self.curr = 0
        self.curr += 1
        self.path_address = self.prev_path[self.curr]
        self.mainArea.setRootIndex(self.mainModel.index(self.path_address))
        self.path.setText(self.path_address.replace("/", "\\"))
        self.leftPane.setCurrentIndex(self.dirModel.index(self.path_address))
        self.leftPane.setFocus()

    def copy(self):
        self.path_main()
        self.temp = self.path_address

    def paste(self):
        try:
            if self.cut_flag:
                self.cutPaste()
                return
            self.path_left()
            if os.path.isdir(self.temp):
                shutil.copytree(self.temp, self.path_address + "/" + os.path.basename(self.temp))
                self.refresh_mainArea()
                return
            shutil.copy2(self.temp, self.path_address)
            self.refresh_mainArea()
        except:
            return

    def cut(self):
        if os.path.isdir(self.temp):
            shutil.move(self.temp, self.path_address + "/" + os.path.basename(self.temp))
            self.refresh_mainArea()
            return
        self.path_main()
        self.temp = self.path_address
        self.cut_flag = True

    def cutPaste(self):
        self.path_left()
        shutil.move(self.temp, self.path_address)
        self.refresh_mainArea()
        self.cut_flag = False

    def rename(self):
        self.path_main()
        dlg = QInputDialog(self.mainArea)
        newname, ok = dlg.getText(self.mainArea, 'Rename', "New Name:", QLineEdit.Normal, "", Qt.Dialog)
        if ok:
            l = len(os.path.basename(self.path_address))
            os.rename(self.path_address, (self.path_address[:l] + newname))
            self.path_address = self.path_address[:l]
            self.index = self.mainModel.index(self.path_address)
            self.refresh_mainArea()

    def darkMode(self):
        if self.darkMode_flag:
            black = "white"
            white = "black"
            self.darkMode_flag = False
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap(":/icons/icons8-moon-and-stars-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.dark_Button.setIcon(icon8)
            self.mainArea.horizontalHeader().show()
        else:
            black = "#212120"
            white = "white"
            self.darkMode_flag = True
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap(":/icons/icons8-sun-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.dark_Button.setIcon(icon8)
            self.mainArea.horizontalHeader().hide()
        
        MainWindow.setStyleSheet(f"background: {black};")
        self.frame.setStyleSheet(f"background: {black};")
        self.path.setStyleSheet(f"color: {white};")
        self.path_label.setStyleSheet(f"font-size: 15px; font-family: Bahnschrift SemiBold; color: {white};")
        self.cut_label.setStyleSheet(f"font-size: 15px; font-family: forte; color: {white}")
        self.copy_label.setStyleSheet(f"font-size: 15px; font-family: forte; color: {white}")
        self.paste_label.setStyleSheet(f"font-size: 15px; font-family: forte; color: {white}")
        self.delete_label.setStyleSheet(f"font-size: 15px; font-family: forte; color: {white}")
        self.newFolder_label.setStyleSheet(f"font-size: 15px; font-family: forte; color: {white}")
        self.leftPane.setStyleSheet(f"background: {black}; color: {white};")
        self.mainArea.setStyleSheet(f"background: {black}; color: {white};")
        self.hideButton.setStyleSheet(f"background: {black}; border: none")

    def enableHidden(self):
        if self.hiddenEnabled == False:
            self.mainModel.setFilter(QDir.NoDotAndDotDot | QDir.Hidden | QDir.AllDirs | QDir.Files)
            self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.Hidden | QDir.AllDirs)
            self.hiddenEnabled = True
        else:
            self.mainModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
            self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
            self.hiddenEnabled = False


import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
