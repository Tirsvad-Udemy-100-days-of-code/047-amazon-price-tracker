# Trin 2: e-mail-alarm

🌐 [English](Step-2-Email-Alert) · **Dansk** · [Bahasa Melayu](Step-2-Email-Alert-ms)

**Opgave.** Når prisen er under en målpris (100), send en e-mail til dig selv med produktets titel, prisen og et link til at købe det. Hold e-mailadresse og adgangskode ude af koden.

**Det vi byggede.** `check_price` sammenligner prisen med `TARGET_PRICE`. `SmtpNotifier` forbinder med `smtplib` på port 587, starter TLS, logger ind og sender beskeden. `SMTP_ADDRESS`, `EMAIL_ADDRESS` og `EMAIL_PASSWORD` læses fra `.env` med `python-dotenv`; `.env.example` viser nøglerne.

Skærmbillederne stammer fra en kørsel, hvor SMTP-forbindelsen er erstattet af en stub, så der blev ikke sendt mail; det andet er tegnet ud fra den besked, koden bygger.

![Kørsel med en SMTP-stub](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-2-run.png)

![Alarmbeskeden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-2-email.png)

**Det vi lærte**

- SMTP-samtalen: connect, `starttls()`, `login()`, `sendmail()`; Gmail kræver en app-adgangskode.
- Miljøvariabler og `.env`-filer holder hemmeligheder ude af repositoryet (`.env` står i `.gitignore`).
- Reglen "under målet" er en lille ren funktion, der er let at teste (under, lig med, over).
- Tests med en falsk SMTP-klasse: testene sender aldrig rigtig mail.
