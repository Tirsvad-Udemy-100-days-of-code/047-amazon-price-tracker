# Trin 4: den levende Amazon-side

🌐 [English](Step-4-Live-Amazon) · **Dansk** · [Bahasa Melayu](Step-4-Live-Amazon-ms)

**Opgave.** Ret koden mod den rigtige Amazon-produktside, og udskriv pris og titel.

**Hvad der skete.** Den 2026-10-28 svarede Amazon botten med HTTP 200 og en robotkontrol-side ("Click the button below to continue shopping") i stedet for produktet. Der var ingen pris at læse.

![Siden Amazon returnerede](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-4-amazon-robot-check.png)

**Det vi byggede.** `is_robot_check` genkender siden, og botten stopper med en tydelig besked. Den forsøger **ikke** at løse eller omgå kontrollen. Selektorer og markører står i `constants.py`; `PRODUCT_URL` i `.env` vælger en anden side, fx øvesiden.

![Botten på den levende side](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-4-run.png)

**Det vi lærte**

- Levende websteder ændrer sig og kan afvise scripts; øvesiden er den pålidelige basis.
- At fejle tydeligt er en del af arbejdet: en præcis fejl slår et traceback eller et forkert tal.
- Respekt for webstedet: ingen omveje uden om en botkontrol.
- Selektorer som data, så en ændring i markup er en enkelt linje.
