# Address Parser

## How to run 
### Docker Compose

```
docker-compose run --build -d 
```

## How to use

## Curl

### Health Check

#### Request

```
curl -X POST -H "Content-Type: application/json" localhost:5000/
```

#### Response

```
{
    "message": "2021-01-22 02:52:17.806643"
}
```

### Parse and address

#### Request

```
curl -X POST -H "Content-Type: application/json" -d '{"address": "77, Bleecker Street"}' localhost:5000/address/parse
```

#### Response

```
{
    "street_name": "Bleecker Street",
    "house_number": "77"
}
```

### Parsed address history

#### Request

```
curl -H "Content-Type: application/json" localhost:5000/address/history
```

#### Response

```
[
    {
        "created_at": "2021-01-22T08:45:57",
        "house_number": "66",
        "street_name": "Calle de las Golondrinas",
        "id": 1
    },
    {
        "created_at": "2021-01-22T08:46:11",
        "house_number": "77",
        "street_name": "Bleecker Street",
        "id": 2
    }
]
```