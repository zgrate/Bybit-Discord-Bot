FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src /code/
COPY .env /code/

ENTRYPOINT ["python3", "main.py"]
