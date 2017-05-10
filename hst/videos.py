import urllib.request
import json

URL = 'http://hubblesite.org/api/v3/videos?page={0}'


def image_from_url(page=1):
    """
    Same as for news releases, the videos are sorted by the publication date and time (last goes first).
    :param page: 
    :return: 
    id	        Internal key to identify the Video. It can be used to gather more information using the details API call (below).
    name	    Name given to the Video
    news_name	Legacy name given to this Video in a news release. Usually is 'a', 'b', 'c', ...
    image	    HTTPS URL of a thumbnail image, 210x118 pixels.
    collection	Collection name the Video belongs to.
    mission	    Space Telescope or telescope website, the Video belongs to. It is usually 'hubble', 'james_webb', etc.    """
    with urllib.request.urlopen(URL.format(page)) as url:
        data = json.loads(url.read().decode())
        return data