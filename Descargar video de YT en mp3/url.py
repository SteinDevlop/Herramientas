class urls:
    def __init__(self,url) -> None:
        self._url = url
    #encapsulamiento de nombre
    @property
    def url(self):
        return self._url
    @url.setter
    def url(self,url):
        self._url = url
    #cierre de encapsulamiento
    def __str__(self):
        return f"{self.url}"