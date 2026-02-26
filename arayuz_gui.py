import sys
import json
import os
import threading
import time # sleep için eklendi, gerçek uygulamada ses dinlerken kullanılabilir

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton,
                             QLabel, QScrollArea, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal, QObject # Sinyaller için QObject ve pyqtSignal eklendi
from PyQt5.QtGui import QFont, QPixmap

# --- Model ve Yardımcı Fonksiyonlar (Gerçek Mantık buraya gelecek) ---
# Buradaki fonksiyonlar, projenizin diğer dosyalarından (örneğin Main3.py'nin kalanı)
# get_bot_response ve sesli komut alımı (command) gibi mantıkları içermelidir.

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2)

# YER TUTUCU: Botun gerçek yanıtını üreten fonksiyon
# Bu fonksiyonun içeriğini kendi bot mantığınıza göre doldurmanız gerekmektedir.
def get_bot_response(user_text):
    """Kullanıcının metnine göre botun yanıtını döndürür."""
    if "merhaba" in user_text.lower():
        return "Merhaba! Size nasıl yardımcı olabilirim?"
    elif "saat kaç" in user_text.lower():
        return f"Şu an saat {time.strftime('%H:%M:%S')}."
    elif "nasılsın" in user_text.lower():
        return "Ben bir yapay zekayım, iyiyim teşekkür ederim. Siz nasılsınız?"
    elif "çıkış" in user_text.lower():
        return "Güle güle! Tekrar görüşmek üzere."
    else:
        return "Üzgünüm, bu komutu anlayamadım. Daha net bir ifade kullanabilir misiniz?"

# YER TUTUCU: Sesli komutları alan fonksiyon (Main3.py'deki command() fonksiyonu gibi)
# Bu fonksiyonun içeriğini kendi ses tanıma mantığınıza göre doldurmanız gerekmektedir.
def command():
    """Sesli komut alır ve metin olarak döndürür."""
    # Bu kısım ses tanıma kodunuzu içerecektir (örneğin, SpeechRecognition kütüphanesi ile)
    print("Dinliyorum...")
    time.sleep(2) # Ses alımı simülasyonu
    # Örnek olarak sabit bir değer döndürüyoruz
    return "saat kaç" # Gerçekte bu, tanınan konuşma metni olacaktır

# --- PyQt5 Arayüz Kodları ---



class LoginWindow(QWidget):
    def __init__(self, switch_to_chat, switch_to_signup):
        super().__init__()
        self.switch_to_chat = switch_to_chat
        self.switch_to_signup = switch_to_signup
        self.setWindowTitle("Giriş Yap")
        self.setGeometry(300, 200, 350, 320)
        self.setStyleSheet("background: #f7fafd;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(16)

        title = QLabel("Life Twin Chatbot - Giriş Yap")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #0078d7;")
        layout.addWidget(title)

        self.email = QLineEdit()
        self.email.setPlaceholderText("E-posta")
        self.email.setFont(QFont("Segoe UI", 12))
        self.email.setStyleSheet("padding: 10px; border-radius: 8px; border: 1px solid #d0d0d0;")
        layout.addWidget(self.email)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Şifre")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFont(QFont("Segoe UI", 12))
        self.password.setStyleSheet("padding: 10px; border-radius: 8px; border: 1px solid #d0d0d0;")
        layout.addWidget(self.password)

        self.login_btn = QPushButton("Giriş Yap")
        self.login_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.login_btn.setStyleSheet("background: #0078d7; color: white; border-radius: 8px; padding: 10px 20px;")
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn)

        self.signup_label = QLabel('<a href="#">Hesabınız yok mu? Kayıt olun</a>')
        self.signup_label.setFont(QFont("Segoe UI", 10))
        self.signup_label.setAlignment(Qt.AlignCenter)
        self.signup_label.setOpenExternalLinks(False)
        self.signup_label.linkActivated.connect(self.switch_to_signup)
        layout.addWidget(self.signup_label)

    def login(self):
        email = self.email.text().strip().lower()
        password = self.password.text().strip()
        users = load_users()
        if email in users and users[email]['password'] == password:
            self.switch_to_chat(email)
        else:
            QMessageBox.warning(self, "Hata", "E-posta veya şifre yanlış.")

class SignupWindow(QWidget):
    def __init__(self, switch_to_login):
        super().__init__()
        self.switch_to_login = switch_to_login
        self.setWindowTitle("Kayıt Ol")
        self.setGeometry(300, 200, 350, 370)
        self.setStyleSheet("background: #f7fafd;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(16)

        title = QLabel("Life Twin Chatbot - Kayıt Ol")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #0078d7;")
        layout.addWidget(title)

        self.email = QLineEdit()
        self.email.setPlaceholderText("E-posta")
        self.email.setFont(QFont("Segoe UI", 12))
        self.email.setStyleSheet("padding: 10px; border-radius: 8px; border: 1px solid #d0d0d0;")
        layout.addWidget(self.email)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Şifre")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFont(QFont("Segoe UI", 12))
        self.password.setStyleSheet("padding: 10px; border-radius: 8px; border: 1px solid #d0d0d0;")
        layout.addWidget(self.password)

        self.password2 = QLineEdit()
        self.password2.setPlaceholderText("Şifre (Tekrar)")
        self.password2.setEchoMode(QLineEdit.Password)
        self.password2.setFont(QFont("Segoe UI", 12))
        self.password2.setStyleSheet("padding: 10px; border-radius: 8px; border: 1px solid #d0d0d0;")
        layout.addWidget(self.password2)

        self.signup_btn = QPushButton("Kayıt Ol")
        self.signup_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.signup_btn.setStyleSheet("background: #0078d7; color: white; border-radius: 8px; padding: 10px 20px;")
        self.signup_btn.clicked.connect(self.signup)
        layout.addWidget(self.signup_btn)

        self.login_label = QLabel('<a href="#">Zaten hesabınız var mı? Giriş yapın</a>')
        self.login_label.setFont(QFont("Segoe UI", 10))
        self.login_label.setAlignment(Qt.AlignCenter)
        self.login_label.setOpenExternalLinks(False)
        self.login_label.linkActivated.connect(self.switch_to_login)
        layout.addWidget(self.login_label)

    def signup(self):
        email = self.email.text().strip().lower()
        password = self.password.text().strip()
        password2 = self.password2.text().strip()
        if not email or not password:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")
            return
        if password != password2:
            QMessageBox.warning(self, "Hata", "Şifreler eşleşmiyor.")
            return
        users = load_users()
        if email in users:
            QMessageBox.warning(self, "Hata", "Bu e-posta ile zaten bir hesap var.")
            return
        users[email] = {"password": password}
        save_users(users)
        QMessageBox.information(self, "Başarılı", "Kayıt başarılı! Şimdi giriş yapabilirsiniz.")
        self.switch_to_login()

class ChatBubble(QLabel):
    def __init__(self, text, is_user=False):
        super().__init__(text)
        self.setWordWrap(True)
        self.setFont(QFont("Segoe UI", 11))
        self.setMargin(10)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        if is_user:
            self.setStyleSheet("background-color: #0078d7; color: white; border-radius: 12px; padding: 8px 12px; margin: 4px 0 4px 40px;")
            self.setAlignment(Qt.AlignRight)
        else:
            self.setStyleSheet("background-color: #f1f0f0; color: #222; border-radius: 12px; padding: 8px 12px; margin: 4px 40px 4px 0;")
            self.setAlignment(Qt.AlignLeft)

# Arka plan iş parçacığından GUI güncellemek için sinyal verici
class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    message_added = pyqtSignal(str, bool)

class ChatWorker(threading.Thread):
    def __init__(self, chat_window_instance, execute_command_func, command_func, input_text=None):
        super().__init__()
        self.chat_window = chat_window_instance
        self.execute_command_func = execute_command_func # Main3.py'deki execute_command fonksiyonu
        self.command_func = command_func # Main3.py'deki command fonksiyonu
        self.input_text = input_text
        self.signals = WorkerSignals()

    def run(self):
        try:
            if self.input_text is None: # Sesli komut ise
                self.signals.message_added.emit("Dinliyorum...", False) # Botun dinlediğini belirt
                query = self.command_func().lower() # Main3.py'deki command() fonksiyonunu kullan
                self.signals.message_added.emit(f"Siz (Sesli): {query}", True) # Kullanıcının sesli komutunu göster
                response = self.execute_command_func(query, self.chat_window) # execute_command'e chat_window'ı ilet
            else: # Metin komutu ise
                self.signals.message_added.emit(f"Siz (Metin): {self.input_text}", True) # Kullanıcının metin mesajını göster
                response = self.execute_command_func(self.input_text, self.chat_window) # execute_command'e chat_window'ı ilet
            
            # execute_command zaten yanıtı arayüze ekliyor olmalı, bu yüzden burada tekrar eklemeye gerek yok.
            # Ancak, eğer execute_command doğrudan yanıt döndürmüyorsa, burada bir ayarlama yapmak gerekebilir.
            # Şimdilik, execute_command içinde arayüz güncellemesi olduğunu varsayıyorum.
           
        except Exception as e:
            self.signals.error.emit(( sys.exc_info()))
        finally:
            self.signals.finished.emit()

class ChatWindow(QWidget):
    def __init__(self, user_email, execute_command_func, command_func):
        super().__init__()
        self.user_email = user_email
        self.execute_command_func = execute_command_func
        self.command_func = command_func

        self.setWindowTitle("Life Twin Chatbot")
        self.setGeometry(200, 100, 480, 640)
        self.setStyleSheet("background: #f7fafd;")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(8)

        # Üst başlık ve çıkış butonu için tek bir QHBoxLayout oluşturuldu
        header_layout = QHBoxLayout()

        # Başlık etiketi
        title = QLabel("Life Twin Chatbot")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #0078d7;")
        header_layout.addWidget(title)

        # Kullanıcı e-posta etiketi
        user_label = QLabel(f"{self.user_email}")
        user_label.setFont(QFont("Segoe UI", 10))
        user_label.setStyleSheet("color: #555; margin-right: 8px;")
        header_layout.addWidget(user_label)
        
        # Bu esnetici, çıkış butonunu sağa iter
        header_layout.addStretch() 

        # Çıkış Butonu Tanımlaması
        self.exit_btn = QPushButton("Çıkış")
        self.exit_btn.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.exit_btn.setStyleSheet("background: #dc3545; color: white; border-radius: 8px; padding: 5px 10px;") # Kırmızı renk uygun
        self.exit_btn.clicked.connect(QApplication.instance().quit) # Tıklandığında uygulamayı kapat
        header_layout.addWidget(self.exit_btn) # Çıkış butonunu header_layout'a ekle

        # Oluşturulan header_layout'ı ana düzene ekle
        main_layout.addLayout(header_layout)

        # Logo ve karşılama mesajı
        logo_label = QLabel()
        if os.path.exists("indir.png"):
            logo_pixmap = QPixmap("indir.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(logo_label)

        welcome_label = QLabel(f"Hoş geldiniz, {self.user_email.split('@')[0]}!")
        welcome_label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("color: #0078d7; margin-bottom: 20px;")
        main_layout.addWidget(welcome_label)

        # Sohbet geçmişi alanı
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border: none;")
        self.chat_content = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_content)
        self.chat_layout.setAlignment(Qt.AlignTop)
        self.scroll.setWidget(self.chat_content)
        main_layout.addWidget(self.scroll, 1)

        # Giriş alanı ve butonlar
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Segoe UI", 12))
        self.input_field.setPlaceholderText("Mesajınızı yazın...")
        self.input_field.setStyleSheet("padding: 10px; border-radius: 8px; border: 1px solid #d0d0d0;")
        self.input_field.returnPressed.connect(self.send_message) # Enter tuşuna basıldığında mesaj gönderme
        input_layout.addWidget(self.input_field, 1)

        self.listen_btn = QPushButton("Dinle")
        self.listen_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.listen_btn.setStyleSheet("background: #28a745; color: white; border-radius: 8px; padding: 10px 20px;")
        self.listen_btn.clicked.connect(self._start_processing_voice_command) # Yeni metod bağlandı
        input_layout.addWidget(self.listen_btn)

        self.send_btn = QPushButton("Gönder")
        self.send_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.send_btn.setStyleSheet("background: #0078d7; color: white; border-radius: 8px; padding: 10px 20px;")
        self.send_btn.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_btn)

        main_layout.addLayout(input_layout)
        self.add_message("Merhaba! Ben Life Twin Chatbot. Size nasıl yardımcı olabilirim?", is_user=False)

    def add_message(self, text, is_user):
        bubble = ChatBubble(text, is_user)
        self.chat_layout.addWidget(bubble)
        self.scroll.verticalScrollBar().setValue(self.scroll.verticalScrollBar().maximum())

    def send_message(self):
        user_text = self.input_field.text().strip()
        if not user_text:
            return
        
        # self.add_message(f"Siz (Metin): {user_text}", is_user=True) # Zaten ChatWorker içinde eklenecek
        self.input_field.clear() # Giriş alanını temizle

        # Arka planda komutu işle
        self._start_processing_command(user_text)

    def _start_processing_command(self, user_input=None):
        """Metin veya sesli komutu işlemek için arka plan iş parçacığı başlatır."""
        self.worker = ChatWorker(self, self.execute_command_func, self.command_func, user_input)
        self.worker.signals.message_added.connect(self.add_message)
        self.worker.signals.error.connect(self._handle_error)
        self.worker.signals.finished.connect(self._processing_finished)
        self.worker.start() # İş parçacığını başlat

    def _start_processing_voice_command(self):
        """Sesli komut işleme sürecini başlatır (user_input=None)."""
        self._start_processing_command(user_input=None)

    def _handle_error(self, error_tuple):
        """Arka plan iş parçacığından gelen hataları işler."""
        ex_type, ex_value, ex_traceback = error_tuple
        QMessageBox.critical(self, "Hata", f"Bir hata oluştu: {ex_value}")
        print(f"Hata: {ex_value}") # Konsola da yazdırılabilir
        # traceback.print_exception(ex_type, ex_value, ex_traceback) # Detaylı hata için

    def _processing_finished(self):
        """Arka plan iş parçacığı tamamlandığında çağrılır."""
        print("Komut işleme tamamlandı.")
        # İsterseniz burada UI elementlerini tekrar etkinleştirebilirsiniz.

# --- Ana Uygulama Başlatma ---

def main_app():
    app = QApplication(sys.argv)
    user_email = "kullanici@example.com"  # Burası gerçek uygulamada login veya config'den gelebilir
    # window = ChatWindow(user_email) # Artık send_text_command ve start_listening parametreleri yok
    # window.show()
    # sys.exit(app.exec_())

if __name__ == "__main__":
    main_app()
