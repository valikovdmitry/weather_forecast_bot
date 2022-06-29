FROM python:3.7
COPY ./services/bot /bot
WORKDIR /bot
RUN pip install -r /bot/requirements.txt
ENTRYPOINT ["python3"]
CMD ["bot.py"]