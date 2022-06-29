FROM python:3.8.6
WORKDIR /usr/src/app

RUN pip install tweepy schedule PyYAML

COPY . .

CMD ["python", "./schedule_bot.py"]
