import requests

class BaseApi:
    BASE_URL = "http://185.240.103.201:8000"
    ENDPOINT = "/api/register"
    HEADERS = {"accept: application/json", "Content-Type: application/json"}

# 1)Авторизация\Регистрация (пользователь)

