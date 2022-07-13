from ui.ui_mainwindow import Ui_MainWindow
from utils.jsonhandler import JsonHandler
from utils.painthander import PaintHandler
from PySide6.QtWidgets import QMainWindow, QLabel, QFileDialog, QMessageBox, QListWidgetItem
from PySide6.QtCore import QDir, Qt, QFileInfo, QFile
from PySide6.QtGui import QPixmap, QKeyEvent
import typing

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("DatasetAssist")
        self.setFocusPolicy(Qt.StrongFocus)
        self.ui.listWidget.setFocusPolicy(Qt.NoFocus)
        self.ui.openPushButton.setFocusPolicy(Qt.NoFocus)
        self.ui.closePushButton.setFocusPolicy(Qt.NoFocus)
        self.ui.savePushButton.setFocusPolicy(Qt.NoFocus)
        self.ui.plotCheckBox.setFocusPolicy(Qt.NoFocus)
        self.ui.jsonCopyCheckBox.setFocusPolicy(Qt.NoFocus)

        self.pathLabel = QLabel(self)
        self.nameLabel = QLabel(self)
        self.copyInfoLabel = QLabel(self)
        self.ui.statusbar.addWidget(self.pathLabel, 0)
        self.ui.statusbar.addWidget(self.nameLabel, 1)
        self.ui.statusbar.addWidget(self.copyInfoLabel, 2)
        self.jsonHandler = JsonHandler()
        self.paintHandler = PaintHandler()
        self.file_folder = ""
        self.dst_folder = ""

        # reset
        self.reset()

        # signal to slot
        self.ui.openPushButton.clicked.connect(self.onOpenButtonClicked)
        self.ui.closePushButton.clicked.connect(self.onCloseButtonClicked)
        self.ui.savePushButton.clicked.connect(self.onSaveButtonClicked)
        self.ui.chooseAllPushButton.clicked.connect(self.onAllChooseButtonClicked)
        self.ui.cancelChooseAllPushButton.clicked.connect(self.onCancelAllChooseButtonClicked)
        self.ui.plotCheckBox.stateChanged.connect(self.onPlotCheckBoxStateChanged)
        self.ui.listWidget.itemSelectionChanged.connect(self.onItemSelectionChange)
    
    def keyPressEvent(self, event:QKeyEvent):
        if event.modifiers() == Qt.NoModifier and event.key() == Qt.Key_J:
            print("next")
            self.handleNextJump()
        elif event.modifiers() == Qt.NoModifier and event.key() == Qt.Key_K:
            print("previous")
            self.handlePreviousJump()
        elif event.modifiers() == Qt.ShiftModifier and event.key() == Qt.Key_J:
            print("5 next")
            self.handleBigNextJump()
        elif event.modifiers() == Qt.ShiftModifier and event.key() == Qt.Key_K:
            print("5 previous")
            self.handleBigPreviousJump()
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_U:
            print("to end")
            self.handleEndJump()
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_I:
            print("to start")
            self.handleStartJump()
        elif event.key() == Qt.Key_P:
            print("plot")
            self.handleCheckPlot()
        elif event.key() == Qt.Key_Space:
            print("space")
            self.handleListItemCheck()

    def getOrigImage(self, image_name:str, is_plot:bool=False) -> QPixmap:
        file_info = QFileInfo()
        # check image path
        image_path = f"{self.file_folder}/{image_name}"
        file_info.setFile(image_path)
        if not file_info.isFile():
            print(f"Image is not exist: {image_path}")
            return
        orig_image = QPixmap(image_path)
        if is_plot:
            # check json path
            json_path = image_path.replace('.jpg', '.json')
            if self.jsonHandler.tryOpenParesJson(json_path):
                # paint
                self.paintHandler.paintByJson(orig_image, self.font(), self.jsonHandler)

        return orig_image

    def showImageByName(self, image_name:str, is_plot:bool=False):
        orig_image = self.getOrigImage(image_name, is_plot)
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
        self.ui.imageLabel.clear()
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

    def reset(self):
        self.ui.openPushButton.setEnabled(True)
        self.ui.closePushButton.setEnabled(False)
        self.ui.jsonCopyCheckBox.setChecked(True)
        self.ui.listWidget.clear()
        self.ui.imageLabel.clear()
        self.file_folder = ""
        self.dst_folder = ""
        self.pathLabel.setText("No Path!!")
        self.nameLabel.setText("    Not Choose!!")
        self.copyInfoLabel.setText("")

    # short key handlers
    def handleCheckPlot(self):
        is_plot = self.ui.plotCheckBox.isChecked()
        self.ui.plotCheckBox.setChecked(not is_plot)
    
    def handleNextJump(self):
        count = self.ui.listWidget.count()
        if count <= 0:
            return
        cur_row = self.ui.listWidget.currentRow()
        if cur_row == count -1:
            return
        cur_row += 1
        self.ui.listWidget.setCurrentRow(cur_row)

    def handlePreviousJump(self):
        count = self.ui.listWidget.count()
        if count <= 0:
            return
        cur_row = self.ui.listWidget.currentRow()
        if cur_row == 0:
            return
        if cur_row == -1:
            cur_row = count - 1
        else:
            cur_row -= 1
        self.ui.listWidget.setCurrentRow(cur_row)

    def handleBigNextJump(self):
        count = self.ui.listWidget.count()
        if count <= 0:
            return
        cur_row = self.ui.listWidget.currentRow()
        if cur_row == count -1:
            return
        cur_row += 5
        if cur_row >= count:
            cur_row = count - 1
        self.ui.listWidget.setCurrentRow(cur_row)

    def handleBigPreviousJump(self):
        count = self.ui.listWidget.count()
        if count <= 0:
            return
        cur_row = self.ui.listWidget.currentRow()
        if cur_row == 0:
            return
        if cur_row == -1:
            cur_row = count - 1
        else:
            cur_row -= 5
        if cur_row < 0:
            cur_row = 0
        self.ui.listWidget.setCurrentRow(cur_row)

    def handleStartJump(self):
        count = self.ui.listWidget.count()
        if count <= 0:
            return
        self.ui.listWidget.setCurrentRow(0)

    def handleEndJump(self):
        count = self.ui.listWidget.count()
        if count <= 0:
            return
        self.ui.listWidget.setCurrentRow(count-1)

    def handleListItemCheck(self):
        cur_row = self.ui.listWidget.currentRow()
        if cur_row == -1:
            return
        cur_item = self.ui.listWidget.item(cur_row)
        check_state = cur_item.checkState()
        if check_state == Qt.Unchecked:
            cur_item.setCheckState(Qt.Checked)
        elif check_state == Qt.Checked:
            cur_item.setCheckState(Qt.Unchecked)

    # slots
    def onOpenButtonClicked(self):
        print("open")
        file_dialog = QFileDialog(self)
        file_folder = file_dialog.getExistingDirectory(self, "Open image folder")
        if file_folder != "":
            self.ui.openPushButton.setEnabled(False)
            self.ui.closePushButton.setEnabled(True)
            self.file_folder = file_folder
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
            self.reset()

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
        # copy files
        file_dialog = QFileDialog(self)
        self.dst_folder = file_dialog.getExistingDirectory(self, "Copy dst image folder")
        if self.dst_folder != "":
            self.copyInfoLabel.setText(f"Copy {len(choosed_images)} images Start...")
            self.copy_files(choosed_images, self.ui.jsonCopyCheckBox.isChecked())
            self.copyInfoLabel.setText(f"Copy {len(choosed_images)} images End!!")

    def onPlotCheckBoxStateChanged(self):
        curItem = self.ui.listWidget.currentItem()
        if curItem is None:
            return
        image_name = curItem.text()
        self.showImageByName(image_name, self.ui.plotCheckBox.isChecked())

    def onItemSelectionChange(self):
        curItem = self.ui.listWidget.currentItem()
        image_name = curItem.text()
        self.nameLabel.setText(f"    Image Name: {image_name}")
        self.showImageByName(image_name, self.ui.plotCheckBox.isChecked())

    def onAllChooseButtonClicked(self):
        count = self.ui.listWidget.count()
        if count <= 0:
            return
        result = QMessageBox.question(self, "Warning", "Choose all image??", QMessageBox.Ok | QMessageBox.Discard, QMessageBox.Discard)
        if result == QMessageBox.Ok:
            for i in range(count):
                item = self.ui.listWidget.item(i)
                if item.checkState() == Qt.Unchecked:
                    item.setCheckState(Qt.Checked)

    def onCancelAllChooseButtonClicked(self):
        count = self.ui.listWidget.count()
        if count <= 0:
            return
        result = QMessageBox.question(self, "Warning", "Cancel Choose all image??", QMessageBox.Ok | QMessageBox.Discard, QMessageBox.Discard)
        if result == QMessageBox.Ok:
            for i in range(count):
                item = self.ui.listWidget.item(i)
                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)