FROM python:3.7-alpine3.11

WORKDIR /app
COPY ./ /app

RUN pip install -r requirements.txt
RUN python setup.py build
RUN chmod +x docker-entrypoints.sh

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoints.sh"]


