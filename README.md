# shopify_admin_dashboard

A small Django app that logs into a Shopify store and shows its products and orders.

## Run locally

Requires Python 3.11+.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in the values, and load them into your shell
python manage.py migrate
DJANGO_DEBUG=1 python manage.py runserver
```

Open <http://localhost:8000>. You are redirected to the Shopify login page.
Run the tests with `python manage.py test`.

## Configuration

Set these as environment variables (`.env` is git-ignored; never commit it):

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET` | Django secret key (required) |
| `SHOPIFY_API_KEY`, `SHOPIFY_API_SECRET` | Credentials from your Shopify app |
| `SHOPIFY_API_VERSION`, `SHOPIFY_API_SCOPE` | Optional; default `unstable` and `read_products,read_orders` |
| `DJANGO_DEBUG` | `1` enables debug mode (off by default) |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hosts; default `localhost,127.0.0.1` |

`pipenv` also works: `pipenv install && pipenv run python manage.py runserver`.
