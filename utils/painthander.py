import random
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPixmap, QPainter, QPen, QFont, QColor
from utils.jsonhandler import JsonHandler

class PaintHandler(object):
    def __init__(self):
        super().__init__()
        self.painter = QPainter()

    def paintByJson(self, orig_image:QPixmap, font:QFont, jsonHandler:JsonHandler, 
                    is_show_content_lst:bool=True):
        count = jsonHandler.getTotalCount()
        text_x = 50
        text_y = 50
        interval = 60
        for i in range(count):
            box = jsonHandler.getBoxByIndex(i)
            class_id = jsonHandler.getClassIdByIndex(i)
            class_name = jsonHandler.getClassNameById(class_id)
            score = jsonHandler.getScoreByIndex(i)
            pred_content = f"{class_name} {score:.3f}"

            self.painter.begin(orig_image)
            self.painter.setPen(QPen(self.getRandomColor(), 5))
            rect = QRect(box[0], box[1], box[2]-box[0], box[3]-box[1])
            self.painter.drawRect(rect)
            font.setPointSize(50)
            self.painter.setFont(font)
            self.painter.drawText(box[0], box[1], pred_content)
            if is_show_content_lst:
                self.painter.drawText(text_x, text_y, pred_content)
                text_y += interval
            self.painter.end()

    def getRandomColor(self) -> QColor:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return QColor(r, g, b, 255)