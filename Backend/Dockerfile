FROM ubuntu:latest
LABEL authors="carter"

RUN apt-get update && apt-get install -y imagemagick
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

EXPOSE 5000
COPY ./api.py /app/api.py
CMD ["python3", "/app/api.py"]