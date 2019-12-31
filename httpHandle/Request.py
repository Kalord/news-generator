import requests

"""
    Класс для выполнения HTTP запросов
    @package http.Request
"""
class Request:
    @staticmethod
    def get(url):
        return requests.get(url).content

    @staticmethod
    def post(url):
        return requests.post(url).content