from url_robots_checker.url_robots_checker import UrlRobotsChecker
from unittest import TestCase
from unittest.mock import MagicMock, patch


class TestUrlRobotsChecker(TestCase):

    def test_empty_url_raises(self):
        self.assertRaises(ValueError, UrlRobotsChecker, "")


    @patch('url_robots_checker.url_robots_checker.reppy')
    @patch('url_robots_checker.url_robots_checker.UrlRobotsPathFinder')
    def test_init(self, mock_finder, mock_rpy):
        UrlRobotsChecker(url='barfoo.com', user_agent='47', request_timeout_seconds=74)
        mock_finder.assert_called_once_with(user_agent='47', request_timeout_seconds=74)
        mock_finder.return_value.find.assert_called_once_with('barfoo.com')

        mock_rpy.Robots.fetch.assert_called_once_with(
            mock_finder.return_value.find.return_value,
            headers={'User-Agent': '47'}
        )

    @patch('url_robots_checker.url_robots_checker.RobotFileParser')
    @patch('url_robots_checker.url_robots_checker.reppy')
    @patch('url_robots_checker.url_robots_checker.UrlRobotsPathFinder')
    def test_can_fetch_no_robots(self, mock_finder, mock_rpy, mock_rfp):
        urc = UrlRobotsChecker(url='barfoo.com', user_agent='47', request_timeout_seconds=74)
        mock_finder.return_value.find.return_value = None
        self.assertTrue(urc.can_fetch('barfoo.com/ssr'))

    @patch('url_robots_checker.url_robots_checker.RobotFileParser')
    @patch('url_robots_checker.url_robots_checker.reppy')
    @patch('url_robots_checker.url_robots_checker.UrlRobotsPathFinder')
    def test_can_fetch_reppy_allowed(self, mock_finder, mock_rpy, mock_rfp):
        mock_rfp.return_value.can_fetch.return_value = False
        urc = UrlRobotsChecker(url='barfoo.com', user_agent='47', request_timeout_seconds=74)
        urc.robots_path = 'http://barfoo.com/robots.txt'
        urc._robots = MagicMock()
        urc._robots.allowed.return_value = True
        self.assertTrue(urc.can_fetch('barfoo.com/ssr'))

    @patch('url_robots_checker.url_robots_checker.RobotFileParser')
    @patch('url_robots_checker.url_robots_checker.reppy')
    @patch('url_robots_checker.url_robots_checker.UrlRobotsPathFinder')
    def test_can_fetch_rfp_allowed(self, mock_finder, mock_rpy, mock_rfp):
        mock_rfp.return_value.can_fetch.return_value = True
        urc = UrlRobotsChecker(url='barfoo.com', user_agent='47', request_timeout_seconds=74)
        urc.robots_path = 'http://barfoo.com/robots.txt'
        urc._robots = MagicMock()
        urc._robots.allowed.return_value = False
        self.assertTrue(urc.can_fetch('barfoo.com/ssr'))

    @patch('url_robots_checker.url_robots_checker.RobotFileParser')
    @patch('url_robots_checker.url_robots_checker.reppy')
    @patch('url_robots_checker.url_robots_checker.UrlRobotsPathFinder')
    def test_can_fetch_rfp_allowed(self, mock_finder, mock_rpy, mock_rfp):
        mock_rfp.return_value.can_fetch.return_value = False
        urc = UrlRobotsChecker(url='barfoo.com', user_agent='47', request_timeout_seconds=74)
        urc.robots_path = 'http://barfoo.com/robots.txt'
        urc._robots = MagicMock()
        urc._robots.allowed.return_value = False
        self.assertFalse(urc.can_fetch('barfoo.com/ssr'))
