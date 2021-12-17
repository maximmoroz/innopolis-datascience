FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
ENV STATIC_URL /static
ENV STATIC_PATH /app/app/static/
COPY ./ /app
RUN pip install -r /app/requirements.txt
