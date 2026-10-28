# Step 2: e-mail alert

🌐 **English** · [Dansk](Step-2-Email-Alert-da) · [Bahasa Melayu](Step-2-Email-Alert-ms)

**Assignment.** When the price is below a target (100), send an e-mail to yourself with the product title, the price and a link to buy it. Keep the e-mail address and password out of the code.

**What we built.** `check_price` compares the price with `TARGET_PRICE`. `SmtpNotifier` connects with `smtplib` on port 587, starts TLS, logs in and sends the message. `SMTP_ADDRESS`, `EMAIL_ADDRESS` and `EMAIL_PASSWORD` are read from `.env` with `python-dotenv`; `.env.example` shows the keys.

The screenshots come from a run where the SMTP connection is replaced by a stub, so no mail was sent; the second one is rendered from the message the code builds.

![Run with a stubbed SMTP connection](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-2-run.png)

![The alert message](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-2-email.png)

**What we gained**

- The SMTP conversation: connect, `starttls()`, `login()`, `sendmail()`; Gmail needs an App Password.
- Environment variables and `.env` files keep secrets out of the repository (`.env` is in `.gitignore`).
- A "below the target" rule that is a tiny pure function and easy to test (below, equal, above).
- Tests with a fake SMTP class: no real mail is ever sent by the tests.
