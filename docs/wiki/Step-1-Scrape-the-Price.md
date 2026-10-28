# Step 1: scrape the price

🌐 **English** · [Dansk](Step-1-Scrape-the-Price-da) · [Bahasa Melayu](Step-1-Scrape-the-Price-ms)

**Assignment.** Use BeautifulSoup to get the price of the Instant Pot on the practice page as a floating point number and print it.

**What we built.** `get_title(html)` and `get_price(html)` in `infrastructure/scraper.py`. The price is in the first element with class `a-offscreen`; its text is `$99.99`. `split("$")` drops the currency sign and `float()` makes the number.

![The practice page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-1-practice-page.png)

![The bot prints the title and the price](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-1-run.png)

**What we gained**

- How to find an element in the browser's inspector and select it with BeautifulSoup (`select_one`).
- How to clean scraped text (`strip`, `split`) before converting it with `float()`.
- Tests that use a saved copy of the page, so they run without the network.
- A clear error (`PriceNotFoundError`) when the element is missing.
