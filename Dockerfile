FROM ubuntu:jammy-20230425

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y default-libmysqlclient-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4500"]