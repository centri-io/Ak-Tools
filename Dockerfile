FROM openjdk:8-alpine

COPY akstage.py /
COPY e3check.py /

CMD "tail -f /dev/null"
