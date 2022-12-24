FROM python:3.7

ENV pythonbuffered=1
ENV DEBUG=False


WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
