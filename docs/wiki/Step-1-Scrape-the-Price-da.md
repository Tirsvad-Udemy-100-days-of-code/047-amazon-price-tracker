# Trin 1: find prisen

🌐 [English](Step-1-Scrape-the-Price) · **Dansk** · [Bahasa Melayu](Step-1-Scrape-the-Price-ms)

**Opgave.** Brug BeautifulSoup til at hente prisen på Instant Pot på øvesiden som et decimaltal og udskriv den.

**Det vi byggede.** `get_title(html)` og `get_price(html)` i `infrastructure/scraper.py`. Prisen står i det første element med klassen `a-offscreen`; teksten er `$99.99`. `split("$")` fjerner valutategnet, og `float()` laver tallet.

![Øvesiden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-1-practice-page.png)

![Botten udskriver titel og pris](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-1-run.png)

**Det vi lærte**

- At finde et element i browserens inspektør og vælge det med BeautifulSoup (`select_one`).
- At rense hentet tekst (`strip`, `split`), før den gøres til tal med `float()`.
- Tests, der bruger en gemt kopi af siden og derfor kører uden netværk.
- En tydelig fejl (`PriceNotFoundError`), når elementet mangler.
