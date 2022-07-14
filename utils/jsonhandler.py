from PySide6.QtCore import QFile, QFileInfo, QJsonParseError, QJsonDocument
from typing import List

class JsonHandler(object):
    def __init__(self):
        super().__init__()

        self._file = QFile()
        self._cls_name_lst = [] # str
        self._class_lst = [] # int
        self._score_lst = [] # float
        self._box_lst = [] #

    def openJsonFile(self, path):
        self._file.close()
        self._file.setFileName(path)
        self._file.open(QFile.ReadOnly | QFile.Text)
        return self._file.isOpen()

    def jsonParse(self):
        if not self._file.isOpen():
            return
        data = self._file.readAll()
        error = QJsonParseError()
        json = QJsonDocument.fromJson(data, error)
        jsonObject = json.object()
        if json.isNull() or json.isEmpty():
            self._cls_name_lst = []
            self._class_lst = []
            self._score_lst = []
            self._box_lst = []
        else:
            self._cls_name_lst = list(jsonObject["cls_names"])
            self._class_lst = list(jsonObject["classes"])
            self._score_lst = list(jsonObject["scores"])
            self._box_lst = list(jsonObject["boxes"])

    def tryOpenParesJson(self, json_path:str) -> bool:
        # check json path
        file_info = QFileInfo()
        file_info.setFile(json_path)
        if not file_info.isFile():
            print(f"Json is not exist: {json_path}")
            return False
        if not self.openJsonFile(json_path):
            print(f"Open json failed: {json_path}")
            return False
        self.jsonParse()
        if not self.checkAllLstCount():
            print(f"Open json count is error: {json_path}")
            return False
        return True

    def getTotalCount(self):
        return len(self._class_lst)
    
    def checkAllLstCount(self) -> bool:
        count = self.getTotalCount()
        if count == 0:
            return False
        if count == len(self._class_lst) and \
           count == len(self._score_lst) and \
           count == len(self._box_lst):
            return True
        else:
            return False
    
    def getClassNameById(self, class_id:int) -> str:
        return self._cls_name_lst[class_id]

    def getClassIdByIndex(self, index:int) -> int:
        return self._class_lst[index]
    
    def getScoreByIndex(self, index:int) -> int:
        return self._score_lst[index]

    def getBoxByIndex(self, index:int) -> List[float]:
        return self._box_lst[index]