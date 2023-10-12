FROM python:3.11.0-slim
WORKDIR /usr/food_calculator/
COPY ./ ./

RUN apt update
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential
RUN pip install poetry==1.5.1
RUN poetry install
