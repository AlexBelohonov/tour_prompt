FROM python:3.7.4

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
#RUN pip install psycopg2
