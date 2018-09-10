From python:2.7-alpine
MAINTAINER yiidtw "yiidtw@gmail.com"
WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080 

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080"]
