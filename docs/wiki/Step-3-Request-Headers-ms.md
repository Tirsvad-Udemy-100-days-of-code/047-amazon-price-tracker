# Langkah 3: header permintaan

🌐 [English](Step-3-Request-Headers) · [Dansk](Step-3-Request-Headers-da) · **Bahasa Melayu**

**Tugasan.** Hantar header seperti pelayar bersama permintaan: sekurang-kurangnya `User-Agent` dan `Accept-Language`.

**Apa yang dibina.** `DEFAULT_HEADERS` dalam `constants.py` (tanpa `Host` dan `X-Amzn-Trace-Id`) dan `RequestsPageFetcher`, yang menghantarnya sebagai `headers=` kepada `requests.get`.

Apa yang pelayar hantar ke httpbin.org/headers, dan apa yang bot hantar (`Host` ditambah oleh `requests`):

![Header yang dihantar oleh pelayar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-3-browser-headers.png)

![Header yang dihantar oleh bot](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-3-bot-headers.png)

**Apa yang kita perolehi**

- Permintaan membawa lebih daripada URL: pelayar, sistem dan bahasa dihantar dalam header.
- Dengan header yang betul, pelayan boleh menjawab dalam bahasa dan mata wang anda.
- Skrip tanpa header kelihatan seperti bot, dan banyak pelayan menyekat bot.
- Satu takrifan header yang baca sahaja, dan ujian yang menyemak apa yang dihantar.
