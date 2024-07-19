from classes.db_toolkil import DBToolkit


class UsersDB(DBToolkit):
    schema = ("id", "name", "summary", "location", "profile_image", "username")

    def __init__(self):
        super().__init__()

    def create_user(self, json: dict):
        data = [json.get(key) for key in self.schema]  # TODO: return of kastil

        sql = (
            "INSERT INTO users ("
            "user_id, "
            "name, "
            "summary, "
            "location, "
            "profile_image, "
            "username "
            ") VALUES (?, ?, ?, ?, ?, ?)"
        )

        self._execute(sql, data)

    def read_user_by_id(self, user_id: int) -> list:
        sql = "SELECT * FROM users WHERE user_id=?"
        result = self._execute(sql, [user_id])

        return result

    def update_user_by_id(self, user_id: int, json: dict):
        data = [json.get(key) for key in self.schema]  # TODO: return of kastil
        data.append(user_id)

        sql = (
            "UPDATE users SET "
            "user_id = ?, "
            "name = ?, "
            "summary = ?, "
            "location = ?, "
            "profile_image = ?, "
            "username = ? "
            "WHERE user_id = ?"
        )
        self._execute(sql, data)

    def delete_user_by_id(self, user_id: int):
        sql = "DELETE FROM users WHERE user_id=?"
        self._execute(sql, [user_id])
