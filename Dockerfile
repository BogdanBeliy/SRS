FROM python:3.9
RUN mkdir /sr_service
WORKDIR /sr_service
COPY . /sr_service
RUN apt-get update && apt-get upgrade
COPY req.txt /sr_service/
RUN pip install -r req.txt

