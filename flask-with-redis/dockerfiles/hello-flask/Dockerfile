FROM python:3.4-alpine

RUN mkdir -p /usr/local/helloworld/

WORKDIR  /usr/local/helloworld/

ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD app.py logging.ini ./

EXPOSE 5000
CMD ["python", "app.py"]
