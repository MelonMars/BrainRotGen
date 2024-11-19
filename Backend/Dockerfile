FROM python:3.11
LABEL authors="carter"

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY ./api.py /app/api.py
CMD ["python3", "/app/api.py"]