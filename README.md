# Bot War Baju

Bot otomatis menggunakan Selenium yang dirancang untuk membeli baju saat flash sale atau war. Bot ini secara otomatis membuka browser Brave, menunggu tombol beli muncul, dan melakukan checkout jika tersedia.

## Fitur

- Standby di halaman countdown produk.
- Klik otomatis tombol beli saat muncul.
- Bisa dikembangkan untuk proses checkout otomatis.

## Kebutuhan Sistem

- Python 3.8+
- Google Chrome / Brave Browser
- ChromeDriver yang sesuai dengan versi browser
- Paket Python:
  - `selenium`
  - `requests`
 
## Penggunaan
1. Buka halaman produk war di browser dan salin URL-nya.
2. Jalankan script:
3.  - `python botwar.py`
4. Bot akan membuka browser Brave dan standby di halaman produk.
5. Saat tombol beli muncul, bot akan mengkliknya.

Note: Untuk checkout otomatis, kamu perlu menambahkan simulasi klik dan pengisian data checkout pada script.

## FAQ
Q: Apakah bot ini bekerja untuk semua situs?
A: Tidak. Bot ini disesuaikan untuk struktur halaman tertentu. Anda harus menyesuaikan selektor HTML jika digunakan untuk situs lain.

Q: Kenapa muncul error session not created?
A: Versi chromedriver tidak cocok dengan versi browser Brave-mu. Coba downgrade browser atau tunggu update chromedriver.

## Instalasi

1. Clone repositori:

```bash
git clone https://github.com/username/bot-war-baju.git
cd bot-war-baju
