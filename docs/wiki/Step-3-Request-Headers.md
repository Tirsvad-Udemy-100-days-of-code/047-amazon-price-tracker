# Step 3: request headers

🌐 **English** · [Dansk](Step-3-Request-Headers-da) · [Bahasa Melayu](Step-3-Request-Headers-ms)

**Assignment.** Send browser-like headers with the request: at least `User-Agent` and `Accept-Language`.

**What we built.** `DEFAULT_HEADERS` in `constants.py` (without `Host` and `X-Amzn-Trace-Id`) and `RequestsPageFetcher`, which passes them as `headers=` to `requests.get`.

What a browser sends to httpbin.org/headers, and what the bot sends (`Host` is added by `requests`):

![Headers sent by a browser](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-3-browser-headers.png)

![Headers sent by the bot](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/047-amazon-price-tracker/raw/branch/main/docs/images/step-3-bot-headers.png)

**What we gained**

- A request carries more than the URL: the browser, the system and the language travel in headers.
- With the right headers a server can answer in your language and currency.
- A script without headers looks like a bot, and many servers block bots.
- One read-only definition of the headers, and tests that check what is sent.
