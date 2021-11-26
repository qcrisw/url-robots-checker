# UrlRobotsChecker

Check if a given URL is allowed to be scraped based on the given website's `robots.txt` rules.

## Usage

```python
from url_robots_checker import UrlRobotsChecker

url = 'foobar.com'
url_robots_checker = UrlRobotsChecker(url)
if not url_robots_checker.can_fetch(url):
    print("Not allowed to scrape")
```
