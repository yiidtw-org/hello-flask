From python:2.7-alpine
MAINTAINER yiidtw "yiidtw@gmail.com"

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080 

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080"]
