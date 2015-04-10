FROM ubuntu:14.04

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install curl libcurl4-openssl-dev ruby ruby-dev make && \
    curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-trusty-td-agent2.sh | sh && \
    apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \
    mkdir -p /data && \
    chmod 755 /data

ADD fluent.conf /etc/fluentd/fluent.conf

EXPOSE 24224

CMD /etc/init.d/td-agent stop && /opt/td-agent/embedded/bin/fluentd -c /etc/fluentd/fluent.conf
