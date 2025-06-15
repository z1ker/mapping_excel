# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QPushButton
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(586, 473)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.actionOpenFolder = QAction(MainWindow)
        self.actionOpenFolder.setObjectName(u"actionOpenFolder")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.actionOpenFolder.setIcon(icon)
        self.actionOpenFolder.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"font: 11pt \"Roboto\";\n"
"color: white;\n"
"background-color: rgb(35, 35, 35);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 420, 591, 51))
        self.pushButton.setStyleSheet(u"background-color: rgba(0, 171, 0,0.1);\n"
"border-radius: 10px;\n"
"qproperty-alignment: AlignCenter;\n"
"font: 500 8pt \"Roboto\";")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 250, 571, 161))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid rgba(133, 125, 250, 0.3);  /* \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 \u0432\u043a\u043b\u0430\u0434\u043e\u043a */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: rgba(133, 125, 250, 0.3);\n"
"    color: white;\n"
"    padding: 1px 20px;\n"
"    border: 1px solid #666;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"

"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgba(133, 125, 250, 0.8);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: 1px solid ;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #555555;\n"
"    color: white;\n"
"}\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.crm_radiobutton_2 = QRadioButton(self.tab)
        self.crm_radiobutton_2.setObjectName(u"crm_radiobutton_2")
        self.crm_radiobutton_2.setGeometry(QRect(10, 50, 241, 20))
        self.crm_radiobutton_2.setStyleSheet(u"QRadioButton {\n"
"    color: white;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #888;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #aaa;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgba(133, 125, 250, 0.3);\n"
"    border: 2px solid rgba(133, 125, 250,0.856);\n"
"}\n"
"")
        self.crm_radiobutton_1 = QRadioButton(self.tab)
        self.crm_radiobutton_1.setObjectName(u"crm_radiobutton_1")
        self.crm_radiobutton_1.setGeometry(QRect(10, 10, 78, 22))
        self.crm_radiobutton_1.setStyleSheet(u"QRadioButton {\n"
"    color: white;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #888;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #aaa;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgba(133, 125, 250, 0.3);\n"
"    border: 2px solid rgba(133, 125, 250,0.856);\n"
"}\n"
"")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(270, 20, 291, 101))
        self.frame.setStyleSheet(u"QFrame#frame {\n"
"    background-color: rgba(133, 125, 250, 0.1);\n"
"    border: 1px solid #5c5c5c;\n"
"    border-radius: 6px;\n"
"}\n"
"QFrame * {\n"
"    background-color: transparent;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(105, 10, 81, 16))
        self.label_6.setStyleSheet(u"background: transparent;")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 242, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background: transparent;")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border: 2px solid rgba(133, 125, 250, 0.3);\n"
"background: transparent;")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.widget1 = QWidget(self.tab_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 241, 121))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tech_radiobutton_1 = QRadioButton(self.widget1)
        self.tech_radiobutton_1.setObjectName(u"tech_radiobutton_1")
        self.tech_radiobutton_1.setStyleSheet(u"QRadioButton {\n"
"    color: white;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #888;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #aaa;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgba(133, 125, 250, 0.3);\n"
"    border: 2px solid rgba(133, 125, 250,0.856);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.tech_radiobutton_1)

        self.tech_radiobutton_2 = QRadioButton(self.widget1)
        self.tech_radiobutton_2.setObjectName(u"tech_radiobutton_2")
        self.tech_radiobutton_2.setStyleSheet(u"QRadioButton {\n"
"    color: white;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #888;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #aaa;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgba(133, 125, 250, 0.3);\n"
"    border: 2px solid rgba(133, 125, 250,0.856);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.tech_radiobutton_2)

        self.tech_radiobutton_3 = QRadioButton(self.widget1)
        self.tech_radiobutton_3.setObjectName(u"tech_radiobutton_3")
        self.tech_radiobutton_3.setStyleSheet(u"QRadioButton {\n"
"    color: white;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #888;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #aaa;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgba(133, 125, 250, 0.3);\n"
"    border: 2px solid rgba(133, 125, 250,0.856);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.tech_radiobutton_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(13, 15, 571, 231))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget2)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(113, 0))
        self.label.setMaximumSize(QSize(113, 50))

        self.horizontalLayout.addWidget(self.label)

        self.widget3 = QWidget(self.widget2)
        self.widget3.setObjectName(u"widget3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_2 = QLineEdit(self.widget3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMaximumSize(QSize(400, 40))
        self.lineEdit_2.setSizeIncrement(QSize(0, 0))
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.pushButtonBrowse = QPushButton(self.widget3)
        self.pushButtonBrowse.setObjectName(u"pushButtonBrowse")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButtonBrowse.sizePolicy().hasHeightForWidth())
        self.pushButtonBrowse.setSizePolicy(sizePolicy3)
        self.pushButtonBrowse.setMaximumSize(QSize(50, 50))
        self.pushButtonBrowse.setStyleSheet(u"background-color: rgba(133, 125, 250, 0.3);\n"
"border-radius: 10px;\n"
"qproperty-alignment: AlignCenter;\n"
"font: 500 8pt \"Roboto\";")

        self.horizontalLayout_3.addWidget(self.pushButtonBrowse)


        self.horizontalLayout.addWidget(self.widget3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.widget_2 = QWidget(self.widget2)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setMaximumSize(QSize(400, 40))

        self.horizontalLayout_4.addWidget(self.lineEdit_3)

        self.pushButtonBrowse_2 = QPushButton(self.widget_2)
        self.pushButtonBrowse_2.setObjectName(u"pushButtonBrowse_2")
        sizePolicy3.setHeightForWidth(self.pushButtonBrowse_2.sizePolicy().hasHeightForWidth())
        self.pushButtonBrowse_2.setSizePolicy(sizePolicy3)
        self.pushButtonBrowse_2.setMaximumSize(QSize(50, 50))
        self.pushButtonBrowse_2.setStyleSheet(u"background-color: rgba(133, 125, 250, 0.3);\n"
"border-radius: 10px;\n"
"qproperty-alignment: AlignCenter;\n"
"font: 500 8pt \"Roboto\";")

        self.horizontalLayout_4.addWidget(self.pushButtonBrowse_2)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(113, 0))
        self.label_5.setMaximumSize(QSize(113, 50))

        self.horizontalLayout_8.addWidget(self.label_5)

        self.widget_3 = QWidget(self.widget2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_5 = QLineEdit(self.widget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy2)
        self.lineEdit_5.setMaximumSize(QSize(400, 40))

        self.horizontalLayout_9.addWidget(self.lineEdit_5)

        self.pushButtonBrowse_4 = QPushButton(self.widget_3)
        self.pushButtonBrowse_4.setObjectName(u"pushButtonBrowse_4")
        sizePolicy3.setHeightForWidth(self.pushButtonBrowse_4.sizePolicy().hasHeightForWidth())
        self.pushButtonBrowse_4.setSizePolicy(sizePolicy3)
        self.pushButtonBrowse_4.setMaximumSize(QSize(50, 50))
        self.pushButtonBrowse_4.setStyleSheet(u"background-color: rgba(133, 125, 250, 0.3);\n"
"border-radius: 10px;\n"
"qproperty-alignment: AlignCenter;\n"
"font: 500 8pt \"Roboto\";")

        self.horizontalLayout_9.addWidget(self.pushButtonBrowse_4)


        self.horizontalLayout_8.addWidget(self.widget_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy4.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy4)
        self.comboBox.setMaximumSize(QSize(16777215, 40))
        self.comboBox.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Excel Mapping", None))
        self.actionOpenFolder.setText(QCoreApplication.translate("MainWindow", u"OpenFolder", None))
#if QT_CONFIG(shortcut)
        self.actionOpenFolder.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+T", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CONVERT", None))
#if QT_CONFIG(tooltip)
        self.crm_radiobutton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043e\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0439 \u0448\u0430\u0431\u043b\u043e\u043d \u0432 \u0441\u0442\u0430\u0440\u0438\u0439 \u0448\u0430\u0431\u043b\u043e\u043d (\u043d\u0435 \u0435\u043a\u0441\u043f\u043e\u0440\u0442\u0438)</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.crm_radiobutton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431'\u0454\u0434\u043d\u0430\u043d\u043d\u044f \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a", None))
        self.crm_radiobutton_1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"CRM", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0441 \u0434\u043e\u043b\u0430\u0440\u0430", None))
        self.tech_radiobutton_1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438", None))
        self.tech_radiobutton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431'\u0454\u0434\u043d\u0430\u043d\u043d\u044f \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a", None))
        self.tech_radiobutton_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438 \u0437 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430\u043c\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"TechSeller", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0444\u0430\u0439\u043b \u0435\u043a\u0441\u043f\u043e\u0440\u0442\u0443 \u0442\u043e\u0432\u0430\u0440\u0443/\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.pushButtonBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0448\u0430\u0431\u043b\u043e\u043d \u0437\u0430 \u044f\u043a\u0438\u043c \u0431\u0443\u0434\u0435 \u0441\u0442\u0432\u043e\u0440\u044e\u0432\u0430\u0442\u0438\u0441\u044c \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.lineEdit_3.setText("")
        self.pushButtonBrowse_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0448\u0430\u0431\u043b\u043e\u043d \u0437\u0430 \u044f\u043a\u0438\u043c \u0431\u0443\u0434\u0435 \u0441\u0442\u0432\u043e\u0440\u044e\u0432\u0430\u0442\u0438\u0441\u044c \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0445\u0430\u0440-\u043a\u0438", None))
        self.lineEdit_5.setText("")
        self.pushButtonBrowse_4.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044e: ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"80087 | \u0412\u0456\u0434\u0435\u043e\u043a\u0430\u0440\u0442\u0438", None))

    # retranslateUi

class AnimatedButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.OutQuad)
        self.original_geometry = None

    def enterEvent(self, event):
        if not self.original_geometry:
            self.original_geometry = self.geometry()

        rect = self.original_geometry.adjusted(-4, -2, 4, 2)  # збільшення
        self.anim.stop()
        self.anim.setStartValue(self.geometry())
        self.anim.setEndValue(rect)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.original_geometry:
            self.anim.stop()
            self.anim.setStartValue(self.geometry())
            self.anim.setEndValue(self.original_geometry)
            self.anim.start()
        super().leaveEvent(event)