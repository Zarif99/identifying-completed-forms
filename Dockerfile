# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /identifying-completed-forms
COPY requirements.txt /identifying-completed-forms/
RUN pip install -r requirements.txt
COPY . /identifying-completed-forms/
