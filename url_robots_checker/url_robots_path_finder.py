
from urllib.parse import SplitResult, urlparse, urlsplit, urlunsplit
import reppy.robots as reppy
from requests import get as requests_get


class UrlRobotsPathFinder:

    def __init__(self, user_agent="*", request_timeout_seconds=30):
        self._user_agent = user_agent
        self._request_timeout_seconds = request_timeout_seconds

    def find(self, url):
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            for scheme in ['https', 'http']:
                processed_url = self._add_scheme_to_url(url, scheme=scheme)
                robots_url = reppy.Robots.robots_url(processed_url)
                if self._is_robots_present(robots_url):
                    return robots_url
            return None

        robots_url = reppy.Robots.robots_url(url)
        if self._is_robots_present(robots_url):
            return robots_url
        return None

    @staticmethod
    def _add_scheme_to_url(url: str, scheme) -> str:
        split_url = urlsplit(url)
        split_result = SplitResult(
            scheme=split_url.scheme or scheme,
            netloc=split_url.netloc or split_url.path,
            path="", query="", fragment=""
        )
        return urlunsplit(split_result)

    def _is_robots_present(self, path: str):
        try:
            result = requests_get(
                path,
                headers={'User-Agent': self._user_agent},
                timeout=self._request_timeout_seconds,
                allow_redirects=True
            )
            return result.ok and urlsplit(result.url).path == '/robots.txt'
        except Exception:  # pylint: disable=broad-except
            return False
