### Machine Learning Homework
by Matvey Vasilev


### Список файлов
0. HW1_Regression_with_inference.ipynb : ноутбук с решенным домашним заданием
1. main.py : Основная программа с реализацией сервиса на FastApi
2. models.py : Файл с основными классами
3. preprocessing.py : Программа для нормализации числовых признаков, кодирования категориальных признаков и загрузки обученной модели
4. encoder_data : энкодер, обученный в ноутбуке
5. scaler_data : скалер, обученный в ноутбуке
6. fitted_model : модель, обученная в ноутбуке
7. predicted_items : тесторые данные для задания 2


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
![image](https://github.com/vmdGH/ml_fastapi_hw/assets/118124570/9fe6b9aa-aefb-4814-b55c-c798705bed55)


### Запрос 2
curl -X 'POST' \
  'http://127.0.0.1:8000/predict_items' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@predict_items.csv;type=text/csv'
![image](https://github.com/vmdGH/ml_fastapi_hw/assets/118124570/ef25de20-88e7-4d69-b329-a4e04fe66c85)

### Комментарии к работе
1. Не хватило времени подготовить данные и подобрать гиперпараметры, чтобы повысить обобщающую способность алгоритма
2. Лучший алгоритм работает с лучшей метрикой r2 примерно равной 0.6
3. Сервис на FastApi получилось реализовать в полной мере

