import sys
from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow, QFileDialog
from excel_ui3 import Ui_MainWindow, AnimatedButton  # Імпорт із згенерованого .py файлу
import pandas as pd
from converter_excel import GoodsProcessor, GoodsProcessor_miners
from PySide6.QtGui import QIcon
class ExcelApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.pushButtonBrowse_3.setVisible(False)
        from PySide6.QtGui import QIcon, QPixmap

        my_pixmap = QPixmap("img/printer.svg")
        my_icon = QIcon(my_pixmap)

        self.setWindowIcon(my_icon)

        self.setFixedSize(self.size())
        self.export_path = ''
        self.import_path = ''
        self.ui.pushButtonBrowse.clicked.connect(self.open_file_without)

        self.ui.pushButtonBrowse_2.clicked.connect(self.open_file)
        # Створення анімованої кнопки
        self.animated_btn = AnimatedButton("CONVERT")
        self.animated_btn.setGeometry(self.ui.pushButton.geometry())
        self.animated_btn.setParent(self.ui.pushButton.parentWidget())
        self.animated_btn.show()
        self.animated_btn.clicked.connect(self.convert_excel)

        # Видалити стару кнопку
        self.ui.pushButton.deleteLater()

        # Перекинути посилання на нову кнопку
        self.ui.pushButton = self.animated_btn
        self.animated_btn.setStyleSheet("""
             QPushButton {
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 10px;
                qproperty-alignment: AlignCenter;
                font: 500 8pt "Roboto";
            }
            QPushButton:hover {
                        background-color: #4b4b7f; /* Трохи світліший при наведенні */
                    }
                    QPushButton:pressed {
                        background-color: #2b2b5d; /* Трохи темніший при натисканні */
                    }
        """)

        # Заміна першої кнопки Browse
        self.animated_browse_btn = AnimatedButton("Browse")
        self.animated_browse_btn.setObjectName("pushButtonBrowse")
        self.animated_browse_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #3b3b6d; /* Темно-фіолетовий */
                        color: white;             /* Білий текст */
                        border: none;
                        border-radius: 10px;      /* Заокруглені краї */
                        padding: 4px 10px;
                        
                    }
                    QPushButton:hover {
                        background-color: #4b4b7f; /* Трохи світліший при наведенні */
                    }
                    QPushButton:pressed {
                        background-color: #2b2b5d; /* Трохи темніший при натисканні */
                    }
                """)
        layout1 = self.ui.pushButtonBrowse.parentWidget().layout()
        if layout1:
            layout1.removeWidget(self.ui.pushButtonBrowse)
            layout1.addWidget(self.animated_browse_btn)
        self.animated_browse_btn.clicked.connect(self.open_file_without)
        self.ui.pushButtonBrowse.deleteLater()
        self.ui.pushButtonBrowse = self.animated_browse_btn

        # Заміна другої кнопки Browse
        self.animated_browse2_btn = AnimatedButton("Browse")
        self.animated_browse2_btn.setObjectName("pushButtonBrowse_2")
        self.animated_browse2_btn.setStyleSheet("""
                            QPushButton {
                                background-color: #3b3b6d; /* Темно-фіолетовий */
                                color: white;             /* Білий текст */
                                border: none;
                                border-radius: 10px;      /* Заокруглені краї */
                                padding: 4px 10px;
                                
                            }
                            QPushButton:hover {
                                background-color: #4b4b7f; /* Трохи світліший при наведенні */
                            }
                            QPushButton:pressed {
                                background-color: #2b2b5d; /* Трохи темніший при натисканні */
                            }
                        """)
        layout2 = self.ui.pushButtonBrowse_2.parentWidget().layout()
        if layout2:
            layout2.removeWidget(self.ui.pushButtonBrowse_2)
            layout2.addWidget(self.animated_browse2_btn)
        self.animated_browse2_btn.clicked.connect(self.open_file)
        self.ui.pushButtonBrowse_2.deleteLater()
        self.ui.pushButtonBrowse_2 = self.animated_browse2_btn


    def show_button(self, checked):
        # checked == True, если RadioButton отмечен
        if checked:
            self.animated_browse3_btn.setVisible(True)
            self.ui.label_4.setVisible(True)
        else:
            self.animated_browse3_btn.setVisible(False)
            self.ui.label_4.setVisible(False)
    def convert_excel(self):
        if not self.export_path or not self.import_path:
            print("⚠️ Будь ласка, оберіть обидва файли.")
            return
        self.selected_sheet_name = self.ui.comboBox.currentText()
        output_file_path = f"goods_{self.selected_sheet_name.split('|')[-1]}.xlsx"

        try:
            if self.ui.crm_radiobutton_1.isChecked():
                processor = GoodsProcessor(
                    export_path=self.export_path,
                    template_path=self.import_path,
                    output_path=output_file_path,
                    template_sheet_name=self.selected_sheet_name
                )
                processor.run()
            elif self.ui.crm_radiobutton_2.isChecked():
                processor = GoodsProcessor(
                    export_path=self.export_path,
                    template_path=self.import_path,
                    output_path=output_file_path,
                    template_sheet_name=self.selected_sheet_name
                )
                processor.load_data()
                processor.process_data_characreristics()
                processor.save_data()

            QMessageBox.information(self, "Успіх", f"Конвертація завершена. Збережено у {output_file_path}")
            print(f"Конвертація завершена. Збережено у {output_file_path}")
        except Exception as e:
            print(f"Помилка при конвертації: {str(e)}")
    def open_file_without(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Оберіть Excel файл",
            "",
            "Excel файли (*.xlsx *.xls);;Усі файли (*)"
        )
        if file_path:
            self.ui.lineEdit_2.setText(file_path.split('/')[-1])
            self.export_path = file_path
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Оберіть Excel файл",
            "",
            "Excel файли (*.xlsx *.xls);;Усі файли (*)"
        )
        if file_path:
            self.ui.lineEdit_3.setText(file_path.split('/')[-1])
            self.load_sheet_names(file_path)
            self.import_path = file_path
    def load_sheet_names(self, file_path):
        try:
            # Отримуємо список аркушів
            xls = pd.ExcelFile(file_path)
            sheet_names = xls.sheet_names  # список назв аркушів

            # Оновлюємо ComboBox
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(sheet_names)

        except Exception as e:
            self.ui.comboBox.clear()
            self.ui.comboBox.addItem(f"Помилка: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelApp()
    window.show()
    sys.exit(app.exec())
