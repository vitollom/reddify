# REDDIfy

A Reddit-clone application where users are able to create communities, post, upvote or downvote posts, and share music using the Spotify API.

## Getting Started

Navigate to https://reddify.herokuapp.com/

OR

Clone down the repository.

```bash
git clone git@github.com:vitollom/reddify.git
```

Install dependencies

```bash
poetry install
```

Create virtual environment

```bash 
poetry shell
```

Run migrations using the command below to create the database.

```bash
python manage.py migrate
```

Last but not least run command below to start server then enjoy site.

```bash
python manage.py runserver
```

## Technologies Used
Python (requests), Django (django-mptt, django-sslserver, django-mathfilters) plus Spotify API integration.

---



