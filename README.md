# PasteBin

A project for GCI 2019

My first project made with [Django](https://www.djangoproject.com/).

## Deploy

1. Generate a secret key `python3 -c "import string, random;open('secret.txt', 'w').write(''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(64)))"`
2. `python3 manage.py migrate`
3. `python3 manage.py runserver`

> LOL I don't know how to deploy this

## TODO

- CSS
- Functionality.
