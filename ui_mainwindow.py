# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fig = MplWidget(self.centralwidget)
        self.fig.setObjectName(u"fig")

        self.horizontalLayout.addWidget(self.fig)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")

        self.verticalLayout.addWidget(self.loadButton)

        self.cleanCheckBox = QCheckBox(self.centralwidget)
        self.cleanCheckBox.setObjectName(u"cleanCheckBox")

        self.verticalLayout.addWidget(self.cleanCheckBox)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.leadComboBox = QComboBox(self.centralwidget)
        self.leadComboBox.setObjectName(u"leadComboBox")

        self.verticalLayout.addWidget(self.leadComboBox)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tFFTSpinBox = QDoubleSpinBox(self.centralwidget)
        self.tFFTSpinBox.setObjectName(u"tFFTSpinBox")
        self.tFFTSpinBox.setDecimals(3)
        self.tFFTSpinBox.setMaximum(2.000000000000000)
        self.tFFTSpinBox.setSingleStep(0.025000000000000)
        self.tFFTSpinBox.setValue(0.250000000000000)

        self.verticalLayout.addWidget(self.tFFTSpinBox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.overlapSpinBox = QDoubleSpinBox(self.centralwidget)
        self.overlapSpinBox.setObjectName(u"overlapSpinBox")
        self.overlapSpinBox.setDecimals(2)
        self.overlapSpinBox.setMinimum(0.000000000000000)
        self.overlapSpinBox.setMaximum(0.950000000000000)
        self.overlapSpinBox.setSingleStep(0.050000000000000)
        self.overlapSpinBox.setValue(0.000000000000000)

        self.verticalLayout.addWidget(self.overlapSpinBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ECG spectrograms", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.cleanCheckBox.setText(QCoreApplication.translate("MainWindow", u"clean", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"lead", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"tFFT [s]", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"overlap ratio", None))
    # retranslateUi

