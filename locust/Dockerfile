FROM python:2.7.9-wheezy
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install libzmq1 && \
    pip install pyzmq locustio fluent-logger && \
    apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \
    mkdir -p /data && \
    chmod 755 /data

EXPOSE 5557 5558 8089 24224

WORKDIR /locust
ADD ./scenarios.py /locust/scenarios.py

RUN chmod -R 755 /locust
