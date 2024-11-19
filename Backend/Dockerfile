FROM ubuntu:latest
LABEL authors="carte"

ENTRYPOINT ["top", "-b"]
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y python3-pip && pip3 install -r /requirements.txt

COPY api.py /app/api.py
CMD ["python3", "/api.py"]