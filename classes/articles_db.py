from classes.db_toolkil import DBToolkit


class ArticlesDB(DBToolkit):
    schema = ("id", "title", "body_markdown", "url", "cover_image", "user_id", "published_at")

    def __init__(self):
        super().__init__()

    def create_article(self, json: dict) -> None:  # TODO: check if article already in base
        data = [json.get(key) for key in self.schema if key != "user_id"]
        data.append(json.get("user", {}).get("user_id"))

        sql = (
            "INSERT INTO articles ("
            "article_id, "
            "title, "
            "text, "
            "url, "
            "cover_image, "
            "published_at, "
            "user "
            ") VALUES (?, ?, ?, ?, ?, ?, ?)"
        )

        self._execute(sql, data)

    def read_article_by_id(self, article_id: int) -> list:
        sql = "SELECT * FROM articles WHERE article_id=?"
        result = self._execute(sql, [article_id])

        return result

    def read_article_by_url(self, url: str) -> list:
        sql = "SELECT * FROM articles WHERE url=?"
        result = self._execute(sql, [url])

        return result

    def read_all_users_articles(self, user_id: int) -> list:
        sql = "SELECT * FROM articles WHERE user=?"
        result = self._execute(sql, [user_id])

        return result

    def update_article_by_id(self, article_id, json: dict) -> None:  # TODO: remake as create
        data = [json.get(key) for key in self.schema]
        data.append(article_id)

        sql = (
            "UPDATE articles SET "
            "article_id = ?, "
            "title = ?, "
            "text = ?, "
            "url = ?, "
            "cover_image = ?, "
            "user = ?, "
            "published_at = ? "
            "WHERE article_id = ?"
        )
        self._execute(sql, data)

    def delete_article_by_id(self, article_id: int) -> None:
        sql = "DELETE FROM articles WHERE article_id=?"
        self._execute(sql, [article_id])
