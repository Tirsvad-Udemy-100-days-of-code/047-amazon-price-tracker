# Langkah 4: halaman Amazon sebenar

🌐 [English](Step-4-Live-Amazon) · [Dansk](Step-4-Live-Amazon-da) · **Bahasa Melayu**

**Tugasan.** Halakan kod ke halaman produk Amazon yang sebenar dan cetak harga serta tajuk.

**Apa yang berlaku.** Pada 2026-10-28 Amazon menjawab bot dengan HTTP 200 dan halaman semakan robot ("Click the button below to continue shopping"), bukan produk. Tiada harga untuk dibaca.

![Halaman yang dikembalikan Amazon](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-4-amazon-robot-check.png)

**Apa yang dibina.** `is_robot_check` mengenali halaman itu dan bot berhenti dengan mesej yang jelas. Ia **tidak** cuba menyelesaikan atau melepasi semakan itu. Pemilih dan penanda ada dalam `constants.py`; `PRODUCT_URL` dalam `.env` memilih halaman lain, contohnya halaman latihan.

![Output bot pada halaman sebenar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-4-run.png)

**Apa yang kita perolehi**

- Laman sebenar berubah dan boleh menolak skrip; halaman latihan ialah asas yang boleh dipercayai.
- Gagal dengan jelas ialah sebahagian daripada kerja: ralat khusus lebih baik daripada traceback atau nombor yang salah.
- Menghormati laman: tiada jalan pintas untuk semakan bot.
- Pemilih disimpan sebagai data, jadi perubahan markup hanyalah satu baris.
