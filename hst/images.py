import urllib.request
import json

URL = 'http://hubblesite.org/api/v3/images?page={0}'


def image_from_url(page=1):
    """
    Same as for news releases, the images are sorted by the publication date and time (last goes first).
    :param page: 
    :return: 
    id	        Internal key to identify the image. It can be used to gather more information using the details API call (below).
    name	    Name given to the Image
    news_name	Legacy name given to this image in a news release. Usually is 'a', 'b', 'c', ...
    collection	Collection name the image belongs to.
    mission	    Space Telescope or telescope website, the image belongs to. It is usually 'hubble', 'james_webb', etc.
    """
    with urllib.request.urlopen(URL.format(page)) as url:
        data = json.loads(url.read().decode())
        return data
