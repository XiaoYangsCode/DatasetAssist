from .ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QLabel, QFileDialog, QMessageBox, QListWidgetItem
from PySide6.QtCore import QDir, Qt, QFileInfo, QFile
from PySide6.QtGui import QPixmap, QImage
import typing

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("DatasetAssist")
        self.ui.jsonCopyCheckBox.setChecked(True)

        self.file_folder = ""
        self.dst_folder = ""
        self.pathLabel = QLabel(self)
        self.pathLabel.setText("No Path!!")
        self.nameLabel = QLabel(self)
        self.nameLabel.setText("    Not Choose!!")
        self.ui.statusbar.addWidget(self.pathLabel, 0)
        self.ui.statusbar.addWidget(self.nameLabel, 1)
        self.ui.listWidget.clear()
        self.ui.imageLabel.clear()
        
        # signal to slot
        self.ui.openPushButton.clicked.connect(self.onOpenButtonClicked)
        self.ui.closePushButton.clicked.connect(self.onCloseButtonClicked)
        self.ui.savePushButton.clicked.connect(self.onSaveButtonClicked)
        self.ui.plotCheckBox.stateChanged.connect(self.onPlotCheckBoxStateChanged)
        self.ui.listWidget.itemSelectionChanged.connect(self.onItemSelectionChange)

    def showImageByName(self, image_name : str):
        image_path = f"{self.file_folder}/{image_name}"

        file_info = QFileInfo(image_path)
        if not file_info.isFile():
            print(f"Image is not exist: {image_path}")
            return

        orig_image = QPixmap(image_path)
        ratio = orig_image.width() / orig_image.height()
        width = self.ui.imageLabel.width()
        height = self.ui.imageLabel.height()
        image_width = 0
        image_height = 0
        if width / height < ratio:
            image_width = width
            image_height = width / ratio
        else:
            image_width = height * ratio
            image_height = height

        image = orig_image.scaled(image_width, image_height)
        self.ui.imageLabel.setPixmap(image)

    def copy_files(self, images:typing.List[str], is_copyjson:bool=False):
        for image in images:
            src_path = f"{self.file_folder}/{image}"
            dst_path = f"{self.dst_folder}/{image}"
            QFile.copy(src_path, dst_path)
            if is_copyjson:
                src_json_path = src_path.replace('.jpg', '.json')
                dst_json_path = dst_path.replace('.jpg', '.json')
                QFile.copy(src_json_path, dst_json_path)

    # slots
    def onOpenButtonClicked(self):
        print("open")
        file_dialog = QFileDialog(self)
        self.file_folder = file_dialog.getExistingDirectory(self, "Open image folder")
        if self.file_folder != "":
            # get file name list
            dir = QDir(self.file_folder)
            file_filters = ["*.jpg"]
            files = dir.entryList(file_filters)
            file_num = len(files)
            self.pathLabel.setText(f"Num: {file_num}    Path: {self.file_folder}")
            # add listwidget
            for file in files:
                item = QListWidgetItem(file)
                self.ui.listWidget.addItem(item)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Unchecked)

    def onCloseButtonClicked(self):
        print("close")
        result = QMessageBox.question(self, "Warning", "Close image folder??", QMessageBox.Ok | QMessageBox.Discard, QMessageBox.Discard)
        if result == QMessageBox.Ok:
            # reset state
            self.ui.listWidget.clear()
            self.ui.imageLabel.clear()
            self.file_folder = ""
            self.dst_folder = ""
            self.pathLabel.setText("No Path!!")
            self.nameLabel.setText("    Not Choose!!")

    def onSaveButtonClicked(self):
        print("save")
        # no choosed tip
        # get all choosed path
        choosed_images = []
        count = self.ui.listWidget.count()
        for i in range(count):
            item = self.ui.listWidget.item(i)
            if item.checkState() == Qt.Checked:
                choosed_images.append(item.text())
        if len(choosed_images) == 0:
            QMessageBox.warning(self, "Warning", "No image has been choosed!!")
            return
        # open dialog to choose path
        # copy files TODO json file
        file_dialog = QFileDialog(self)
        self.dst_folder = file_dialog.getExistingDirectory(self, "Copy dst image folder")
        if self.dst_folder != "":
            self.copy_files(choosed_images, self.ui.jsonCopyCheckBox.isChecked())

    def onPlotCheckBoxStateChanged(self):
        print(self.ui.plotCheckBox.isChecked())

    def onItemSelectionChange(self):
        curItem = self.ui.listWidget.currentItem()
        image_name = curItem.text()
        self.nameLabel.setText(f"    Image Name: {image_name}")
        self.showImageByName(image_name)




