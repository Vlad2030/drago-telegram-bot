FROM python:3.11-slim

COPY . /drago-bot
# COPY .env /sniper-bot

WORKDIR /drago-bot/

ENV PYTHONDONTWRITEBYTECODE 1
ENV TELEGRAM_BOT_TOKEN None
ENV DRAGO_CONTRACT_ADDRESS 5D9LBmEeWjKXZs8JRaP8YdBDdkdQPwu9mATXTcMUq7YU

RUN pip install -r requirements.txt
