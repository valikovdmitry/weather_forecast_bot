FROM python:3.7
COPY ./services/weather_server /weather_server
WORKDIR /weather_server
RUN pip install -r /weather_server/requirements.txt
ENV FLASK_APP /weather_server/weather_server.py
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["weather_server.py"]




