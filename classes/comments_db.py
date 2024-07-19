from classes.db_toolkil import DBToolkit


class CommentsDB(DBToolkit):
    schema = ("id_code", "text", "user")

    def __init__(self):
        super().__init__()

    def create_comment(self, json: dict):
        data = [json.get(key) for key in self.schema if key != "user"]
        data.append(json.get("user", {}).get("user_id"))

        sql = "INSERT INTO comments (" "id_code, " "text, " "user " ") VALUES (?, ?, ?)"

        self._execute(sql, data)

    def read_comment_by_id_code(self, id_code: str) -> list:
        sql = "SELECT * FROM comments WHERE id_code=?"
        result = self._execute(sql, [id_code])

        return result

    def read_all_users_comments(self, user_id: int) -> list:
        sql = "SELECT * FROM comments WHERE user=?"
        result = self._execute(sql, [user_id])

        return result

    def update_comment_by_id_code(self, id_code: str, json: dict):
        data = [json.get(key) for key in self.schema if key != "user"]
        data.append(json.get("user", {}).get("user_id"))
        data.append(id_code)

        sql = "UPDATE comments SET " "id_code = ?, " "text = ?, " "user = ? " "WHERE id_code = ?"
        self._execute(sql, data)

    def delete_comment_by_id_code(self, id_code: str):
        sql = "DELETE FROM comments WHERE id_code=?"
        self._execute(sql, [id_code])
