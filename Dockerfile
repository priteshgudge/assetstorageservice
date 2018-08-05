FROM ubuntu:14.04

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

#ADD requirements.txt /app
COPY .  /app

WORKDIR /app
ENV HOME /app
RUN pip3 install -r requirements.txt

ENV ENVIRONMENT=development
ENV PYTHONPATH=/app/

EXPOSE 7500

ENTRYPOINT [ "assetstorageservice/conf/entrypoint.sh"]
#CMD [ "python","./assetstorageservice/conf/service_app.py" ]
