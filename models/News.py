import random
from httpHandle.Request import Request
from xmlHandle.Parser import Parser

"""
    Модель для работы с новостями
    @package models.News
"""
class News:
    """
        Сервис с новостями
    """
    link = 'https://lenta.ru/rss/news'

    @staticmethod
    def newsKey():
        return 'guid'

    @staticmethod
    def filter(data):
        result = []
        for item in data:
            if News.newsKey() in item:
                result.append(item)
        return result

    @staticmethod
    def getAll():
        news = Parser.run(Request.get(News.link))
        return News.filter(news)

    @staticmethod
    def getRandomNews():
        news = News.getAll()
        keys = ['title', 'description']
        result = {}

        for key in keys:
            item = random.choice(news)
            result[key] = item[key]
        
        return result