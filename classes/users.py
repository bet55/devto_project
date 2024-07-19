from classes.devto_api_toolkit import DevToApiToolkit


class User(DevToApiToolkit):
    USERS_URL = "https://dev.to/api/users"

    def __init__(self):
        super().__init__()

    def get_user_by_id(self, user_id: int) -> dict:
        url = f"{self.USERS_URL}/{user_id}"
        response = self._make_request("GET", url)
        return response
