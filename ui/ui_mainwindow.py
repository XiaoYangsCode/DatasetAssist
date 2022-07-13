# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 702)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.editorGroupBox = QGroupBox(self.centralwidget)
        self.editorGroupBox.setObjectName(u"editorGroupBox")
        self.verticalLayout = QVBoxLayout(self.editorGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.openPushButton = QPushButton(self.editorGroupBox)
        self.openPushButton.setObjectName(u"openPushButton")

        self.horizontalLayout.addWidget(self.openPushButton)

        self.savePushButton = QPushButton(self.editorGroupBox)
        self.savePushButton.setObjectName(u"savePushButton")

        self.horizontalLayout.addWidget(self.savePushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.jsonCopyCheckBox = QCheckBox(self.editorGroupBox)
        self.jsonCopyCheckBox.setObjectName(u"jsonCopyCheckBox")

        self.horizontalLayout_4.addWidget(self.jsonCopyCheckBox)

        self.plotCheckBox = QCheckBox(self.editorGroupBox)
        self.plotCheckBox.setObjectName(u"plotCheckBox")

        self.horizontalLayout_4.addWidget(self.plotCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.chooseAllPushButton = QPushButton(self.editorGroupBox)
        self.chooseAllPushButton.setObjectName(u"chooseAllPushButton")

        self.verticalLayout.addWidget(self.chooseAllPushButton)

        self.cancelChooseAllPushButton = QPushButton(self.editorGroupBox)
        self.cancelChooseAllPushButton.setObjectName(u"cancelChooseAllPushButton")

        self.verticalLayout.addWidget(self.cancelChooseAllPushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.closePushButton = QPushButton(self.editorGroupBox)
        self.closePushButton.setObjectName(u"closePushButton")

        self.verticalLayout.addWidget(self.closePushButton)


        self.verticalLayout_2.addWidget(self.editorGroupBox)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.imageLabel)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 6, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 6, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.line_5 = QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 1, 1, 1, 1)

        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)

        self.line_6 = QFrame(self.groupBox)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 0, 3, 1, 1)

        self.line_7 = QFrame(self.groupBox)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 1, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)

        self.line_8 = QFrame(self.groupBox)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 0, 5, 1, 1)

        self.line_9 = QFrame(self.groupBox)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 1, 5, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(2, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.editorGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Editor", None))
        self.openPushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.jsonCopyCheckBox.setText(QCoreApplication.translate("MainWindow", u"JsonCopy", None))
        self.plotCheckBox.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.chooseAllPushButton.setText(QCoreApplication.translate("MainWindow", u"ChooseAll", None))
        self.cancelChooseAllPushButton.setText(QCoreApplication.translate("MainWindow", u"CancelChooseAll", None))
        self.closePushButton.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.imageLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Readme", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Previous 5: shift+k", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Check plot: p", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Previous: k", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Choose one: space ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Next 5: shift+j", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Next: j", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"To end: ctrl+u", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"To start: ctrl+i", None))
    # retranslateUi

