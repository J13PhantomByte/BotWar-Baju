import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import requests

# --- SETTINGS ---
URL = 'https://calledelarache.com/'  # Ganti dengan URL countdown
TELEGRAM_TOKEN = '7233952987:AAEDEr9uPIqecNmbSPu2IWM7O11DK5kxuZA'
TELEGRAM_CHAT_ID = '6532672072'
CHROMEDRIVER_PATH = 'C:/Users/siapa/Downloads/chromedriver-win64/chromedriver.exe'  # Pastikan chromedriver sesuai versi Brave (Chromium)
BRAVE_PATH = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # <- Sesuaikan path Brave kamu
WAKTU_WAR = '18:05:00'

# --- FUNGSI NOTIFIKASI TELEGRAM ---
def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
        requests.post(url, data=data)
    except:
        print("Gagal kirim ke Telegram.")

# --- SETUP BROWSER DENGAN BRAVE ---
options = Options()
options.binary_location = BRAVE_PATH
options.add_argument(r"--user-data-dir=C:\temp\brave-profile-selenium")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)


driver.get(URL)
print("Bot standby di halaman countdown...")

# --- TUNGGU HINGGA WAKTU WAR ---
while True:
    now = datetime.now().strftime("%H:%M:%S")
    if now >= WAKTU_WAR:
        break
    time.sleep(0.5)

print("Mencoba klik tombol...")
clicked = False

# --- CARI TOMBOL DAN KLIK ---
while not clicked:
    try:
        tombol = driver.find_element(By.XPATH, "//button[contains(text(), 'Shop Now')]")
        tombol.click()
        clicked = True
        print("Tombol diklik! Masuk halaman checkout...")
        send_telegram("Tombol Shop Now diklik! Menuju checkout...")
    except NoSuchElementException:
        time.sleep(0.1)

# --- TUNGGU QRIS / CHECKOUT MUNCUL ---
try:
    time.sleep(3)  # Waktu loading halaman checkout
    qris = driver.find_element(By.TAG_NAME, 'img')  # Sesuaikan jika QRIS dalam elemen lain
    if qris:
        print("QRIS ditemukan. Siap dibayar.")
        send_telegram("QRIS ditemukan! Segera bayar sebelum kehabisan!")
except:
    print("QRIS tidak ditemukan, mungkin halaman belum siap.")
