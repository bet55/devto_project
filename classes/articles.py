import requests

from classes.devto_api_toolkit import DevToApiToolkit


class Article(DevToApiToolkit):
    MY_ARTICLES_URL = "https://dev.to/api/articles/me/all"
    ARTICLES_URL = "https://dev.to/api/articles"

    def __init__(self):
        super().__init__()

    def get_article_by_path(self, url: str) -> dict:
        url = url.replace("https://dev.to", "https://dev.to/api/articles")
        response = self._make_request("GET", url)
        return response

    def get_article_by_id(self, article_id: int) -> dict:
        url = f"{self.ARTICLES_URL}/{article_id}"
        response = self._make_request("GET", url)
        return response

    def get_my_articles(self) -> dict:
        response = self._make_request("GET", self.MY_ARTICLES_URL)
        return response

    def get_pictures_from_my_articles(self) -> dict:
        articles = self.get_my_articles()
        pictures_from_my_articles = {}
        for article in articles:
            pictures_from_my_articles = {article["id"]: article["cover_image"]}
        return pictures_from_my_articles
