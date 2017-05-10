import urllib.request
import json

URL = 'http://hubblesite.org/api/v3/image/{}'


def image_details_from_url(image):
    """
    :param image ID: 
    :return:
    name	Title given to the Image
    description	Image description text, caption
    credits	Image's credits and acknowledgments
    news_name	Legacy name given to this Image in a news release. Usually is 'a', 'b', 'c', ...
    mission	Space Telescope or telescope website, the Image belongs to. It is usually 'hubble', 'james_webb', etc.
    collection	Collection name the Image belongs to.
    image_files	Array of downloadable image files. It could be images, PDFs, ZIP files containing images, etc. Each element containing:
        file_url: HTTPS URL of the image file.
        file_size: Size of the file.
        width: Width of the image, if it is a common image file format
        height: Height of the image, if it is an image file
    """
    with urllib.request.urlopen(URL.format(image)) as url:
        data = json.loads(url.read().decode())
        return data



