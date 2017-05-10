import urllib.request
import json

URL = 'http://hubblesite.org/api/v3/glossary/{}'


def term_from_url(term):
    """
    Glossary of Astronomy terms
    :param term: 
    :return:
    definition	Definition text.
    """
    with urllib.request.urlopen(URL.format(term)) as url:
        data = json.loads(url.read().decode())
        return data
