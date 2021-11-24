from urllib.robotparser import RobotFileParser
import reppy.robots as reppy
from .url_robots_path_finder import UrlRobotsPathFinder


class UrlRobotsChecker:

    def __init__(self, url: str, user_agent="*", request_timeout_seconds=30, **kwargs):
        if not url:
            raise ValueError('Url cannot be empty')

        self._url = url
        self._user_agent = user_agent
        self._request_timeout_seconds = request_timeout_seconds
        self.robots_path = UrlRobotsPathFinder(**kwargs).find(self._url)
        self._robots = self._fetch_robots()

    def can_fetch(self, url):
        return not self.robots_path \
            or self._robots.allowed(url, self._user_agent) \
            or self._can_robotparser_fetch_url(url)

    def _can_robotparser_fetch_url(self, url: str):
        robot_file_parser = RobotFileParser(self.robots_path)
        robot_file_parser.read()
        return robot_file_parser.can_fetch(self._user_agent, url)

    def _fetch_robots(self):
        if self.robots_path:
            return reppy.Robots.fetch(self.robots_path, headers={'User-Agent': self._user_agent})
        return None
