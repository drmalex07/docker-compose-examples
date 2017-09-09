FROM debian:jessie-slim

RUN  apt-get update && apt-get install -y rsyslog

VOLUME [ "/var/log", "/etc/rsyslog.d" ]

COPY ./rsyslog.conf /etc/rsyslog.conf

EXPOSE 514 514/udp 

CMD rsyslogd -n
