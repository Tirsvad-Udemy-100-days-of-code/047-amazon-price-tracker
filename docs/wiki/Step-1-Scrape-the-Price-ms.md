# Langkah 1: ambil harga

🌐 [English](Step-1-Scrape-the-Price) · [Dansk](Step-1-Scrape-the-Price-da) · **Bahasa Melayu**

**Tugasan.** Gunakan BeautifulSoup untuk mendapatkan harga Instant Pot di halaman latihan sebagai nombor perpuluhan dan cetaknya.

**Apa yang dibina.** `get_title(html)` dan `get_price(html)` dalam `infrastructure/scraper.py`. Harga berada dalam elemen pertama dengan kelas `a-offscreen`; teksnya `$99.99`. `split("$")` membuang simbol mata wang dan `float()` menghasilkan nombor.

![Halaman latihan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-1-practice-page.png)

![Bot mencetak tajuk dan harga](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-1-run.png)

**Apa yang kita perolehi**

- Cara mencari elemen dalam pemeriksa pelayar dan memilihnya dengan BeautifulSoup (`select_one`).
- Cara membersihkan teks yang diambil (`strip`, `split`) sebelum menukarnya dengan `float()`.
- Ujian yang menggunakan salinan halaman yang disimpan, jadi ia berjalan tanpa rangkaian.
- Ralat yang jelas (`PriceNotFoundError`) apabila elemen tiada.
