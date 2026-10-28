# Step 4: the live Amazon page

🌐 **English** · [Dansk](Step-4-Live-Amazon-da) · [Bahasa Melayu](Step-4-Live-Amazon-ms)

**Assignment.** Point the code at the real Amazon product page and print the price and the title.

**What happened.** On 2026-10-28 Amazon answered the bot with HTTP 200 and a robot-check page ("Click the button below to continue shopping"), not the product. There was no price to read.

![The page Amazon returned](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-4-amazon-robot-check.png)

**What we built.** `is_robot_check` recognises that page and the bot stops with a clear message. It does **not** try to solve or get past the check. Selectors and markers are in `constants.py`; `PRODUCT_URL` in `.env` chooses another page, for example the practice page.

![Output of the bot on the live page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-4-run.png)

**What we gained**

- Live sites change and may refuse scripts; the practice page is the reliable baseline.
- Failing clearly is part of the job: a specific error beats a traceback or a wrong number.
- Respect for the site: no workarounds for a bot check.
- Selectors kept as data, so a markup change is a one-line edit.
