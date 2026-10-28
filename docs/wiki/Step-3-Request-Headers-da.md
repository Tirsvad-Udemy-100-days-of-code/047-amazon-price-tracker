# Trin 3: request headers

🌐 [English](Step-3-Request-Headers) · **Dansk** · [Bahasa Melayu](Step-3-Request-Headers-ms)

**Opgave.** Send browser-lignende headers med forespørgslen: mindst `User-Agent` og `Accept-Language`.

**Det vi byggede.** `DEFAULT_HEADERS` i `constants.py` (uden `Host` og `X-Amzn-Trace-Id`) og `RequestsPageFetcher`, der sender dem som `headers=` til `requests.get`.

Det en browser sender til httpbin.org/headers, og det botten sender (`Host` tilføjes af `requests`):

![Headers sendt af en browser](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-3-browser-headers.png)

![Headers sendt af botten](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-3-bot-headers.png)

**Det vi lærte**

- En forespørgsel rummer mere end adressen: browser, system og sprog rejser med i headers.
- Med de rette headers kan en server svare på dit sprog og i din valuta.
- Et script uden headers ligner en bot, og mange servere blokerer bots.
- Én skrivebeskyttet definition af headers og tests, der kontrollerer, hvad der sendes.
