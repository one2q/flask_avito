FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip inctall -r requirements.txt
COPY instance instance
COPY migrations migrations
COPY . .

CMD flask run -h 0.0.0.0 -p 80
