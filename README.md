# 💰 Dolar-hoy API

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ac8a7b4797024d109d59994c531a8375)](https://app.codacy.com/gh/jd-apprentice/dolar-hoy-api?utm_source=github.com&utm_medium=referral&utm_content=jd-apprentice/dolar-hoy-api&utm_campaign=Badge_Grade)

![IMG](https://wallpapercave.com/wp/wp3105546.png)

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

## 🧰 Stack

- Python
- FastAPI
- Docker
- PlanetScale
- GitHub Actions
- DigitalOcean
- Nginx