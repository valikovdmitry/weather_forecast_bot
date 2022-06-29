FROM python:3.7
COPY . /weather_server
WORKDIR /weather_server
RUN pip install -r requirements.txt
ENV FLASK_APP /weather_server/weather_server.py
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["weather_server.py"]




