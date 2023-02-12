# gerekli kütüphaneler dahil edildi.
import sys
import os
from PyQt5.QtCore import QLocale, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QTextCursor, QFont
from PyQt5.QtWidgets import QAction
from pyqt.Notepad_projesi import new_window # Aynı dizinde bulunan başka modülü aktarmak iin nokta kullan.

# Bir tane pencere üzerinde kullanılacak widgetler için class oluşturuldu.
class Notepad(QWidget): # QWidget sınıfını miras alarak içerisinde bulunan özellikleri kullanabilir.

    def __init__(self):
        super().__init__()  # Qwidget örnek niteliklerini alması için gerekli.
        self.init_ui()  # Oluşturulan fonksiyonun daima çalışması için gerekli. Çünkü bir sınıfta
                        # ilk önce init fonksiyonu aktif olur.

    def init_ui(self): # Pencerenin içerisinde bulunacak buton, text alanı gibi widgetların yerleşimi için gereken fonksiyon

        self.text = QTextEdit()     # bir tane text alanı oluşturduk.
        self.text.setPlaceholderText("Not defterine hoşgeldin...")  # Karşılama metni oluşturur.
        self.text.setFont(QFont("Times New Roman", 12))
        self.text.setLocale(QLocale(QLocale.Turkish))   # Dili türkçe yapar.
        self.text.setAlignment(Qt.AlignBottom)  # Yazıları sağa ve sola yaslar.
        h_box = QHBoxLayout() # Pencereye yatay olarak yerleşmesi için boxlayout oluşturduk.
        h_box.addWidget(self.text)  # Widget'i layout'a ekledik.
        self.setLayout(h_box)   # Widget'i pencere üzerinde göstermek için layout'u pencereye ekledik.

    # Functions
    def news(self):
        self.text.clear()

    def new_window(self):
        self.new = Mainwindow() #Qwidget üzerinden işlem yaptığım için self kullandım. Çünkü self Qwidget objesini temsil eder.

    def dosya_ac(self):
        # Dosya yolunu ve _ ile bool değerini alma.
        self.file_name = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))
        # Bilgisyarda bulunan dosya dizinini getenv() içerisine parametre olarak vermek gerekiyor. Bu da o dizine gidip dosya
        # yolunu file_name' e atıyor (demet halinde döner).
        # ('C:/Users/Yusuf KAYA/PycharmProjects/pythonProject/PyQt5/Notepad_projesi/nett.py', 'All Files (*)') bu tarz.
        with open(self.file_name[0], "r") as file:
            self.text.setPlainText(file.read())

    def save_file(self):
        #file_name, _= QFileDialog.getSaveFileName(self, "Kaydet", os.getenv("HOME"))
        # ('C:/Users/Yusuf KAYA/Desktop/sds', 'All Files (*)') dosyanın kaydedileceği yolu (path) file_name içerisine atıyorum.

        if self.file_name is None: # Bu dosya yoluna sahip bir dosya yoksa farklı kaydet fonksiyonuna yönlerdirdim
            return self.save_as()

        else:
            with open(self.file_name[0], "w") as file:
                file.write(self.text.toPlainText())
                qApp.quit()


    def save_as(self):
        file_name = QFileDialog.getSaveFileName(self, "Kaydet", os.getenv("HOME"))
        with open(file_name[0], "w") as file:
            file.write(self.text.toPlainText())
            qApp.quit()


    def sayfa_yapisi(self):
        self.new_win = new_window.Sayfayapisi()
         # Qwidget üzerinden işlem yaptığım için self kullandım. Çünkü self Qwidget objesini temsil eder.

    # diğer menü
    def geri_al(self):
        pass

    def kopya(self):
        pass


    def yapistir(self):
        self.text.insertPlainText(self.write)   # Seçilen yazıları tekrar cümle sonuna yapıştırır.

    def tum_sec(self):
        self.text.selectAll()   # Tüm yazıyı seçtiğini göstermesi için gerekli.
        cursor = self.text.textCursor() # Text wigdet' için imleç tanımlıyorum.
        QTextCursor(cursor).movePosition(QTextCursor.EndOfLine) # imleci aktif hale getirebilmek için QTextCursor()' da cursor' parametre olarak kullanıyorum.
        self.text.setTextCursor(cursor) # Qtextedit üzerinde imleci görünür yapmak için kullanıyorum.
        self.write = self.text.toPlainText()    # textedit' te bulunan tüm yazıları seçer.





# Ana pencere
class Mainwindow(QMainWindow):  # Ana pencere, bir uygulamanın kullanıcı arabirimini oluşturmak için bir çerçeve sağlar.
                                # Ana pencere yönetimi için QMainWindow sınıfını miras alması gerekiyor.
    def __init__(self):
        super().__init__()
        self.notepad = Notepad()    # Burada yukarıda ki sınıfı ve içerisindekileri kullanabilmek için örneklendirdim.
        # Ve bu örneği kullanarak yukarıdaki sınıfta bulunan özellikleri yani Text alanını ana pencerenin merkezine yerleştirdim.
        self.setCentralWidget(self.notepad) # Kullanmak istediğin widget'i ana pencerenin merkezine koymak için kullanırsın.
        self.menuler()

    def menuler(self):

        menus = self.menuBar()# Ana pencereye menü çubuğu ekler. Bu işlev, menü çubuğu yoksa boş bir menü çubuğu döndürür.

        # Menuler
        file = menus.addMenu("Dosya")   # Menü çubuğuna yeni menüler ekledim.
        edit = menus.addMenu("Düzen")
        style = menus.addMenu("Biçim")
        view = menus.addMenu("Görünüm")

        # File's Actions
        new = QAction("Yeni", self)
        new.setShortcut("Ctrl + O")
        file.addAction(new) # Bu eklediğim aksiyonların kısayollarını ekledim.
        new_window = file.addAction("Yeni pencere")
        new_window.setShortcut("Ctrl + Shift + N")
        dosya_ac = file.addAction("Dosya Aç")
        dosya_ac.setShortcut("Ctrl + O")
        save = file.addAction("Kaydet")
        save.setShortcut("Ctrl + S")
        save_as = file.addAction("Farklı kaydet")
        save_as.setShortcut("Ctrl + Shift + S")
        page = file.addAction("Sayfa yapısı")
        exitt = file.addAction("Çıkış")
        exitt.setShortcut("Ctrl + Q")

        # Edit's Actions
        back = edit.addAction("Geri Al")
        back.setShortcut("Ctrl + Z")
        cut = edit.addAction("Kes")
        cut.setShortcut("Ctrl + X")
        copy = edit.addAction("Kopyala")
        copy.setShortcut("Ctrl + C")
        paste = edit.addAction("Yapıştır")
        paste.setShortcut("Ctrl + V")
        delete = edit.addAction("Sil")
        delete.setShortcut("Del")
        select_all = edit.addAction("Tümünü seç")
        select_all.setShortcut("Ctrl + A")
        date_hour = edit.addAction("Saat ve Tarih")
        date_hour.setShortcut("F5")

        # Style's Actions
        style.addAction("Sözcük Kaydır")
        style.addAction("Yazı tipi")

        # View's Actions
        zoom_in = view.addMenu("Yakınlaştır")
        zoom_in.addAction("Yakınlaştır")
        zoom_in.addAction("Uzaklaştır")
        zoom_in.addAction("Varsayılana dön")
        status = view.addAction("Durum çubuğu")
        status.setCheckable(True)   # Eklenen bir aksiyonu aktif ya da değil özelliği eklemek için kullandım.

        file.triggered.connect(self.response)  # triggered eklenen aksiyonlara fonksiyon atayabilmek için
        # ara bağlantı olarak düşünülebilir.
        edit.triggered.connect(self.response2)

        self.setGeometry(1200, 250, 500, 500)  # Pencerenin pc ekranında nerede açılacağını ve boyutunu, genişliğini
        # ele alan fonksiyon.
        self.setWindowTitle("Notepad")  # Pencerenin başlığını değiştirmek için kullandım.
        self.setWindowIcon(QIcon("notepaddd.png"))  # Pencerenin iconunu değiştirmek için kullandım.

        self.show()  # İşleri ve pencereyi görüntülemeye yarar.

    # Action's Functions
    def response(self, action):

        if action.text() == "Yeni":
            self.notepad.news()

        elif action.text() == "Yeni pencere":
            self.notepad.new_window()

        elif action.text() == "Dosya Aç":
            self.notepad.dosya_ac()

        elif action.text() == "Kaydet":
            self.notepad.save_file()

        elif action.text() == "Farklı kaydet":
            self.notepad.save_as()

        elif action.text() == "Sayfa yapısı":
            self.notepad.sayfa_yapisi()

        else:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon("notepaddd.png"))

            if action.text() == "Çıkış":
                cev = msg.question(self, "Uyarı", "Kayıt yapılsın mı?", QMessageBox.Yes | QMessageBox.No)
                if cev == QMessageBox.Yes:
                    self.notepad.save_file()
                    qApp.quit()

    def response2(self, action):

        if action.text() == "Geri Al":
            self.notepad.geri_al()

        elif action.text() == "Kopyala":
            self.notepad.kopya()

        elif action.text() == "Yapıştır":
            self.notepad.yapistir()

        elif action.text() == "Tümünü seç":
            self.notepad.tum_sec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = Mainwindow()
    sys.exit(app.exec())
