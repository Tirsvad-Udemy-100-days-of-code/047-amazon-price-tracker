# Langkah 2: amaran e-mel

🌐 [English](Step-2-Email-Alert) · [Dansk](Step-2-Email-Alert-da) · **Bahasa Melayu**

**Tugasan.** Apabila harga di bawah sasaran (100), hantar e-mel kepada diri sendiri dengan tajuk produk, harga dan pautan untuk membelinya. Jauhkan alamat e-mel dan kata laluan daripada kod.

**Apa yang dibina.** `check_price` membandingkan harga dengan `TARGET_PRICE`. `SmtpNotifier` menyambung dengan `smtplib` pada port 587, memulakan TLS, log masuk dan menghantar mesej. `SMTP_ADDRESS`, `EMAIL_ADDRESS` dan `EMAIL_PASSWORD` dibaca daripada `.env` dengan `python-dotenv`; `.env.example` menunjukkan kuncinya.

Tangkapan skrin datang daripada larian yang sambungan SMTP-nya diganti dengan stub, jadi tiada e-mel dihantar; yang kedua dilukis daripada mesej yang dibina oleh kod.

![Larian dengan stub SMTP](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-2-run.png)

![Mesej amaran](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-2-email.png)

**Apa yang kita perolehi**

- Perbualan SMTP: connect, `starttls()`, `login()`, `sendmail()`; Gmail memerlukan kata laluan aplikasi.
- Pemboleh ubah persekitaran dan fail `.env` menjauhkan rahsia daripada repositori (`.env` ada dalam `.gitignore`).
- Peraturan "di bawah sasaran" ialah fungsi tulen yang kecil dan mudah diuji (bawah, sama, atas).
- Ujian dengan kelas SMTP palsu: ujian tidak pernah menghantar e-mel sebenar.
