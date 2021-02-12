FROM python:3.7.7 as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY manage.py ./manage.py
COPY crio_xmeme ./crio_xmeme
COPY Xmeme ./Xmeme

EXPOSE 8081


FROM production as development

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .

