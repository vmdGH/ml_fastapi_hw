# ml_fastapi_hw
Machine Learning Homework


### Запрос 1
curl -X 'POST' \
  'http://127.0.0.1:8000/predict_item/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "bmw",
    "year": 2010,
    "km_driven": 10000,
    "fuel": "Petrol",
    "seller_type": "Individual",
    "transmission": "Manual",
    "owner": "First Owner",
    "mileage": "23.01 kmpl",
    "engine": "999 CC",
    "max_power": "67 bhp",
    "torque": "91Nm@ 4250rpm",
    "seats": 5.0
}'

### Запрос 2
curl -X 'POST' \
  'http://127.0.0.1:8000/predict_items' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@predict_items.csv;type=text/csv'
