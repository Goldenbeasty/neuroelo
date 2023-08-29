# Neuroelo

This is somehow working well, run `tests/test_rating_system.py` for some examples

## How it works?

We count the words in a message, it gets multiplied by a constant that we set, then the message is multiplied by the normalized and weighed compression rateo of the string through gzip.

This works and like quite well.

## How to get the website

requirements: a (unix like) shell, `python3` and `tailwindcss`

go to [website](./website) and run `create_website.sh` the website root will be created at `website/neuroelo_web/`
