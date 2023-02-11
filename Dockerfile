FROM python:3.10.2-slim-bullseye
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
WORKDIR /pay_system
COPY . .
RUN pip install -r requirements.txt