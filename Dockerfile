FROM ubuntu:kinetic

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip=22.0.2+dfsg-1ubuntu0.2 \
    && apt-get install -y default-libmysqlclient-dev=1.0.8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4500"]