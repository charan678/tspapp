FROM python:3.8-slim

WORKDIR /app
COPY ./ /app

RUN pip install -r requirements.txt
RUN python setup.py test
RUN python -m pytest
RUN chmod +x docker-entrypoints.sh

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoints.sh"]


