FROM python:3.9.9

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt 

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt 


COPY . /app/

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]

EXPOSE 8000


