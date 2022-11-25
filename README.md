# SocialFeed

![Python](https://img.shields.io/badge/Python-3.10-green?style=flat)

> An image-bookmarking social application


## Bare metal setup

This project requires that you have [redis](https://redis.io/) installed and running on your host machine.
After the install, modify your `/etc/hosts` file and adjust it as below:

```bash
# /etc/hosts
127.0.0.1 socialfeed.com
```

Clone the repo, install dependencies and run the project.
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver_plus --cert-file cert.crt
```

## It just works(Docker setup) - Work in progress

You can get the project up and running out of hte box and ready for development or production as below.

**Development**

With *docker* and *docker-compose* installed , clone the repo and run the following command at teh root of the project.
```bash
docker-compose -f docker-compose.yml up -d --build

```

**Production**

```bash
docker-compose -f docker-compose.prod.yml up -d --build

```

> Access the project via: **127.0.0.1:8000/account** or **socialfeed.com:8000/account**


### Note
For easy use of this project,create a bookmark on the *bookmark* bar of your browser by dragging the button at the *account* page.
Visit any site and click on the bookmark to select the image to bookmark. Happy tagging!