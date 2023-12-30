FROM python:3.11-slim

COPY . /sniper-bot
# COPY .env /sniper-bot

WORKDIR /sniper-bot/

ENV PYTHONDONTWRITEBYTECODE 1
ENV TELEGRAM_BOT_TOKEN None
ENV BOT_SKIP_UPDATE True
ENV BACKEND_HOST 0.0.0.0
ENV BACKEND_PORT 8001

RUN pip install -r requirements.txt
