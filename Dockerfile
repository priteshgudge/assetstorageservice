FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

COPY . /root/assetstorageservice

WORKDIR /root/assetstorageservice

CMD [ "pip install", "-r", "./assetstorageservice/conf/requirements.txt"]

#ENV ENV_PATH=/root
ENV ENVIRONMENT=development
ENV PYTHONPATH=/root/assetstorageservice

EXPOSE 7500

ENTRYPOINT ["./assetstorageservice/conf/entrypoint.sh"]
#CMD [ "python","./assetstorageservice/conf/service_app.py" ]