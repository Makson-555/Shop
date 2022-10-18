FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /famshop

WORKDIR /famshop

COPY requirements.txt /famshop/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /famshop/