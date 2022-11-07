FROM python:3.9.6-alpine as python

# working directory
WORKDIR /social-feed

# environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# psycopg deps
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# build stage 2
FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
COPY . ./
RUN poetry install --no-interaction --no-ansi -vvv


FROM python as runtime
ENV PATH="/social-feed/.venv/bin:$PATH"
COPY --from=poetry /social-feed /social-feed
EXPOSE 8000
CMD




