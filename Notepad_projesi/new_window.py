from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.a = QComboBox(self)  # Qwidget tarafından oluşturulan pencere üzerine
        # yerleştirmek için parametre olarak self kullandım.

        self.a.addItems(["Python", "Java", "JavaScript", "Php", "C#", "C"])
        self.a.setFont(QFont("Times New Roman", 12))
        self.a.setMouseTracking(True)   # Listeyi görüntülemeden combobox üzeriden fare ile değişim yapabiliyorum.
        self.a.setMaxVisibleItems(5)
        self.a.move(50, 20)

        pal = self.a.palette()
        pal.setColor(QPalette.Window, QColor("background-color: blue"))
        self.a.setPalette(pal)


class Sayfayapisi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.n = window()
        self.setCentralWidget(self.n)

        self.setGeometry(500, 500, 450, 200)
        self.setWindowIcon(QIcon("notepaddd.png"))
        self.setWindowTitle("Sayfa yapısı")
        self.show()

