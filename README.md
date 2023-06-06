# 💰 Dolar-hoy API

![IMG](https://wallpapercave.com/wp/wp3105546.png)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/15bdc445d90b4f1492b8a3254edef844)](https://app.codacy.com/gh/jd-apprentice/dolar-hoy-api/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

<a href="https://www.digitalocean.com/?refcode=dea6443429a5&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg" alt="DigitalOcean Referral Badge" /></a>

## 📝 Description

Project to learn how to deploy and mantain a REST API using FastAPI and Docker.
The API is a simple GET endpoint that returns the current value of the dolar in Argentina.
Values are being scrapped from [DolarHoy](https://www.dolarhoy.com/) and saved in PlanetScale.

## 🏃 Run

To run the project you need to have Docker installed in your machine. Then, you can run the following command:

```bash 
docker compose up
```

## 🧪 Endpoints

```bash
GET /dolar/:currency
POST /manual
```

Where `:currency` can be

- blue
- oficial
- crypto
- mep


## 🖥 Examples

```bash
curl -X GET "http://localhost:4500/dolar/blue" -H  "accept: application/json"
```

Response
```json
{
  "label": "Dolar Blue",
  "prices": {
    "buy_price": 488,
    "sell_price": 493
  },
  "last_update": "2023-05-25 20:35:58" // UTC -3
}
```

## 🌻 Workflow

![image](https://github.com/jd-apprentice/dolar-hoy-api/assets/68082746/4791c037-aae9-459d-b9dc-0db5b1d296aa)

## 🧰 Stack

- Python
- FastAPI
- Docker
- PlanetScale
- GitHub Actions
- DigitalOcean
- Nginx

## 🔒 Environment Variables

| Name | Description | Default |
| HOST | Host to run the API | xxx |
| USERNAME | Username to connect to PlanetScale | xxx |
| PASSWORD | Password to connect to PlanetScale | xxx |
| DATABASE | Database to connect to PlanetScale | xxx |
| MANUAL_USERNAME | Username to use the scrapper | xxx |
| MANUAL_PASSWORD | Password to use the scrapper | xxx |