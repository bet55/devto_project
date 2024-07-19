import hashlib
from abc import ABC

import dotenv
import requests

from classes.caching import Caching
from exeptions.app import ApplicationException
from exeptions.devto import DevToException


def _extract_api_token() -> str:
    try:
        api_key = dotenv.get_key(dotenv.find_dotenv(raise_error_if_not_found=True), "API_TOKEN")
    except IOError as e:
        raise ApplicationException(e)

    if not api_key:
        raise ApplicationException("empty .env API_TOKEN")

    return api_key


class DevToApiToolkit(ABC):
    _SUCCESSFUL_CODES = (
        200,
        201,
    )
    _CACHE_TTL = 60 * 5
    _CACHE_STORAGE_PATH = "cache"

    def __init__(self):
        self._api_token = _extract_api_token()
        self._cache = Caching(self._CACHE_STORAGE_PATH, self._CACHE_TTL)

    def _make_request(self, method: str, url: str, body: dict = None) -> dict:
        string = method + url + str(body)
        cache_key = hashlib.md5(string.encode("utf-8")).hexdigest()
        cache_value = self._cache.get_cache(cache_key)
        if cache_value:
            return cache_value

        try:
            response = requests.request(method, url, json=body, headers={"api-key": self._api_token})
        except requests.RequestException as e:
            raise DevToException(e)

        if response.status_code not in self._SUCCESSFUL_CODES:
            raise DevToException(response.text)

        if not response.json():
            raise DevToException("empty response")

        result = response.json()

        self._cache.set_cache(cache_key, result)
        return result
