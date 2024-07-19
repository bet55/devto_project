# TODO: higher lvl functions
# TODO: flake8
import json

from flask import Flask, request

from classes import Article, Comment
from classes.caching import Caching
from classes.articles_db import ArticlesDB

fantastic_article = "https://dev.to/taylorye/ye-left-moscow-why-ghi"

# entry point
# a_db = ArticlesDB()
# a = Article()
# c = Caching()
# c.clear_cache()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/articles/<int:article_id>")
def _get_article(article_id):
    article_db = ArticlesDB()
    result = article_db.read_article_by_id(article_id)[0]
    result_json = {article_db.schema[i]: result[i + 1] for i in range(len(article_db.schema))}
    return result_json


@app.post("/articles")
def _post_article():
    article_id = request.json.get("article_id", False)
    if not article_id:
        return "<p>Missing article id</p>", 400

    article_module = Article()
    article = article_module.get_article_by_id(article_id)
    if not article:
        return "<p>Article not found</p>", 404

    article_db = ArticlesDB()
    article_db.create_article(article)
    return "<p>Success</p>", 200


# TODO: delete article from base by id
