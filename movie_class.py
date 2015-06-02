# create a class, which has movie title, storylinr, poster-image-url, 
# and youtube movie trailer as his property.
class Movies():
    def __init__(self, m_title, m_storyline, m_image, m_trailer):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = m_image
        self.trailer_youtube_url = m_trailer