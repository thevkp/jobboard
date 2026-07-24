## What is a "config file" and why do we need one?
Your app needs values that change depending on where it's running — database URL, secret keys, debug flags, API keys. You never want these hardcoded in your code because:
- You DB URL is different on your laptop vs a teammate's machine vs production.
- Secrets(passwords, API keys) should never be committed to git.
The standard pattern: put actula values in a `.env` file (which is gitignored), and have Python read them into a typed object at startup. That's what `Settings` is — a single object `os.getenv("DATABASE_URL")` calls everywhere.

