FROM python3.8

CMD apt-get 

COPY akstage.py /
COPY e3check.py /

CMD tail -f /dev/null
