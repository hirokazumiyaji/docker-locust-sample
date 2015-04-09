FROM python:2.7.9-wheezy
RUN apt-get -y update && \
    apt-get -y install libzmq1 && \
    pip install pyzmq locustio && \

EXPOSE 5557 5558 8089

WORKDIR /locust
ADD . /locust

RUN chmod -R 755 /locust

ENTRYPOINT ["locust"]
