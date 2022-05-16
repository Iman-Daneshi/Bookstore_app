# pull base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRIGHTBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# install dependencies
RUN python3 -m venv /books/books_env
RUN PATH="/books/books_env/bin:$PATH"

COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

#copy project
COPY . /code/

