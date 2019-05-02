FROM python:alpine

LABEL maintainer="Jon Borgonia <jon@gomagames.com>"

RUN pip install requests bs4

WORKDIR /app

COPY linkchecker.py /app/

RUN chmod +x /app/linkchecker.py

ENTRYPOINT ["/app/linkchecker.py"]
