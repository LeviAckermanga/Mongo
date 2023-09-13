FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install Flask pymongo

EXPOSE 5000

CMD ["python", "app.py"]