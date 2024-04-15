FROM python:3.12.3-alpine

WORKDIR /app

# Copy only the requirements file first, to leverage Docker cache
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . /app

EXPOSE 8000 62922 49554