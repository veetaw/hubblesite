import urllib.request
import json

URL = 'http://hubblesite.org/api/v3/news?page={0}'


def news_from_url(page=1):
    """
    List of published releases, produced by the Office of Public Outreach of the Space Telescope Science Institute.
    All those news releases are present at HubbleSite's news center, at http://hubblesite.org/news.

    They are sorted by the publication date and time (the last release will be the first).
    :param page: 
    :return:
    news_id	Internal key to identify the release. It can be used to gather more information using the details API call (below).
    name	Title of the News Release
    url	    http://hubblesite.org URL of the news release

    """
    with urllib.request.urlopen(URL.format(page)) as url:
        data = json.loads(url.read().decode())
        return data
