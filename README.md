# Social Feed

> An image-sharing social application


## Setup
This project uses [poetry](https://python-poetry.org/docs/) for dependency management.
Clone the repo, install dependencies and run the project.

```bash
poetry install
poetry shell
python manage.py runserver
```


## It just works(Docker setup)

**Development**

With *docker* and *docker-compose* installed , clone the repo and run the following command at teh root of the project.
```bash
docker-compose -f docker-compose.yml up -d --build

```

**Production**

```bash
docker-compose -f docker-compose.prod.yml up -d --build

```

Access the project via: 1**27.0.0.1:8000/home**%  