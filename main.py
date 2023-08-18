from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
twitter_bot = """
#############################################################
#                      Twitter  BOT                         #
############################################################# 
#                           Oku                             #
#############################################################
#        Sisteme hiçbir bilginiz kaydedilmektedir           #
#   Bu Yüzden bot başlayınca bilgileriniz girilmelidir.     #
#   Saatlerce sizin için textleriniz resim ve videolar ile  #
#                  Paylaşabilirim                           #
#############################################################
"""
print(twitter_bot)
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')
# Headless tarayıcı ayarları
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # GPU kullanımını devre dışı bırak
# Selenium ile tarayıcıyı başlat
driver = webdriver.Chrome(options=chrome_options)
print("Bot Aktifleştirildi Lütfen Bekleyin")
driver.get("https://twitter.com/i/flow/login")
time.sleep(2)
# Kullanıcı adı ve şifre girişi
username = input("Kullanıcı Adı : ")
password = input("Şifre: ")
try :
#Kullanıcı adı ve şifre girişleri
    driver.find_element("name", "text").send_keys(username)
    span_element = driver.find_element(By.XPATH, "//span[text()='Next']")
    # Elemente tıkla
    span_element.click()
    time.sleep(1)
    
    driver.find_element("name", "password").send_keys(password)
    span_element = driver.find_element(By.XPATH, "//span[text()='Log in']")
    span_element.click()
    time.sleep(2)
    # Başarılı giriş yaptı
    twitter_terminal_login_panel_ico = """
    #############################################################
    #                Başarılı Şekilde Giriş Yapıldı             #
    #############################################################
    """

    print( twitter_terminal_login_panel_ico)
except : 
    print("Lütfen Kullanıcı adı şifreyi kontrol edin , (İnternet bağlantını unutma :) )") 


# Başarılı giriş yaptı

print("Botunuzun ve klosörünüzün bulunduğu pathını çift slash ile ekleyin örn :  C:\\Users\\ben\\Desktop\\twet ")
ana_dosya = input("Path : ")

while 1:
    # Dosya Yolları
    base_folder = ana_dosya
    image_folder = os.path.join(base_folder, "resim")
    text_folder = os.path.join(base_folder, "yazi")
    video_folder = os.path.join(base_folder, "video")

    # Dosya listelerini alın
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".png")])
    text_files = sorted([f for f in os.listdir(text_folder) if f.endswith(".txt")])
    video_files = sorted([f for f in os.listdir(video_folder) if f.endswith(".mp4")])

    # İlgili dosya türlerini eşleştirerek işleme koymak
    for txt_file in text_files:
        base_name = os.path.splitext(txt_file)[0]  # Dosya adını al

        # Metni al
        with open(os.path.join(text_folder, txt_file), 'r', encoding='utf-8') as txt:
            text_content = txt.read().strip()

        # Eşleşen resim ve video dosyasını al
        img_file = f"{base_name}.png"
        video_file = f"{base_name}.mp4"

        if img_file in image_files:
            img_path = os.path.join(image_folder, img_file)
            # Resmi tweet'e ekleme işlemleri
            input_file_element = driver.find_element(By.XPATH, '//input[@type="file"]')

            # Dosya yolunu input elementine gönderin
            input_file_element.send_keys(img_path)
            time.sleep(5) 
            gonderilen_mesaj_onayi_ico = """
            #############################################################
            #                   Twettiniz Gönderildi :)                 #
            #############################################################
            """
            print(gonderilen_mesaj_onayi_ico)
	        
            
            
        if video_file in video_files:
            video_path = os.path.join(video_folder, video_file)
            # Videoyu tweet'e ekleme işlemleri
            input_file_element = driver.find_element(By.XPATH, '//input[@type="file"]')

            # Dosya yolunu input elementine gönderin
            input_file_element.send_keys(video_path)
            time.sleep(60) 
            gonderilen_mesaj_onayi_ico = """
            #############################################################
            #                   Twettiniz Gönderildi :)                 #
            #############################################################
            """
            print(gonderilen_mesaj_onayi_ico)
            

        # İşlemi tamamla ve tweet'i gönder
        for veri in text_content.split('\n'):
            # Mevcut içeriği temizle
            input_element = driver.find_element("css selector", '[aria-label="Tweet text"]')
            input_element.send_keys(veri.strip())
            time.sleep(1)  # İşlemin tamamlanması için bir süre bekle

        input_file_element = driver.find_element(By.XPATH, '//input[@type="file"]')
            # Dosya yolunu input elementine gönderin
        time.sleep(3) 
        element = driver.find_element("xpath", '//div[@data-testid="tweetButtonInline"]')
        element.click()
        time.sleep(2)

        driver.get("https://twitter.com/home")
        time.sleep(2)

    gonderilen_mesaj_onayi_ico = """
            #############################################################
            #                   Dosyalar Gönderildi....                 #
            #############################################################
            """
    print(gonderilen_mesaj_onayi_ico)

    secim = int(input("Çıkmak için 1 e basınız"))
    if secim == 1:
        break

# Tarayıcıyı kapat
driver.quit()
