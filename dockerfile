FROM python:3.12.0-slim
WORKDIR /usr/food_calculator/
COPY ./ ./

RUN apt update
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential
RUN pip install poetry
RUN poetry install
