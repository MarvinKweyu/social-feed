# Social Feed

> An image-sharing social application


## Setup
Clone the repo, install dependencies and run the project.

```bash
pip install -r requirements.txt
python manage.py migrate
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