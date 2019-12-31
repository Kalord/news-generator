from models.News import News

def main():
    news = News.getRandomNews()
    print(news['title'])
    print(news['description'])

if __name__ == '__main__':
    main()