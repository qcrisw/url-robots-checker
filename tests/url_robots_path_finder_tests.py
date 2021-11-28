from url_robots_checker.url_robots_path_finder import UrlRobotsPathFinder
from unittest import TestCase
from unittest.mock import patch, Mock


class TestUrlRobotsPathFinder(TestCase):

    def _mock_robots_url(_, url):
        return f'{url}/robots.txt'

    def _mock_head(*args, **kwargs):
        response_mock = Mock()
        response_mock.ok = True
        response_mock.url = args[1]
        return response_mock

    @patch('url_robots_checker.url_robots_path_finder.requests_get')
    @patch('url_robots_checker.url_robots_path_finder.reppy')
    def test_can_find(self, mock_rpy, mock_rh):
        mock_rpy.Robots.robots_url.side_effect = self._mock_robots_url
        mock_rh.side_effect = self._mock_head

        urc = UrlRobotsPathFinder().find('foobar.com')
        self.assertTrue(urc == 'https://foobar.com/robots.txt')
