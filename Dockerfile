# pull official base image
FROM ubuntu
# set working directory
WORKDIR /usr/src/social-feed

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
# DON'T BUFFER STDOUT AND STDERR
ENV PYTHONUNBUFFERED 1

RUN  apt update
RUN apt install postgresql postgresql-contrib
RUN  systemctl start postgresql.service

# psycopg deps
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

RUN echo "modify hosts"
RUN sudo echo "127.0.0.1 socialfeed.com" > /etc/hosts
RUN echo "done with hosts"
# copy entrypoint
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/social-feed/entrypoint.sh
RUN chmod +x /usr/src/social-feed/entrypoint.sh
# copy project
COPY . .
RUN ls /usr/src/social-feed

# run entrypoint
ENTRYPOINT [ "/usr/src/social-feed/entrypoint.sh" ]
