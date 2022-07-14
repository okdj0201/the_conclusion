FROM python:3.11.0b4-slim
WORKDIR /usr/src/app

RUN pip install tweepy schedule PyYAML

COPY . .

#CMD ["python", "./schedule_bot.py"]
