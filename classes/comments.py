from classes.devto_api_toolkit import DevToApiToolkit


class Comment(DevToApiToolkit):
    COMMENTS_URL = "https://dev.to/api/comments"

    def __init__(self):
        super().__init__()

    def get_comment_by_id(self, comment_id: str) -> dict:
        url = f"{self.COMMENTS_URL}/{comment_id}"
        response = self._make_request("GET", url)
        return response

    def get_comments_by_article_id(self, article_id: int) -> dict:
        url = f"{self.COMMENTS_URL}?a_id={article_id}"
        response = self._make_request("GET", url)
        return response
