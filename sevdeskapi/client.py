import requests


class SevDeskClient:
    """
        Initialize a Client who manage the Connections to the SevDesk API Endpoint
    """

    def __init__(self, api_token=None, base_url="https://my.sevdesk.de", version="v1"):
        assert api_token is not None

        self._api_token = api_token
        self._base_url = base_url
        self._version = version

    def create(self, *model_list):
        for model in model_list:
            model.use_sevclient(self)
            model.controller().create()

    def build_url(self, base_url=None, version=None, model=None, **kwargs):
        """
            Build a url used for Request by given arguments

            :param base_url: Custom URL that should be requested; If None the SevDeskClient base_url attribute would be used
            :param version: Custom API Version which should be used; If None the SevDeskClient version attribute would be used
            :param model: Required. Model which should be used for Request
            :return:
        """
        if base_url is None:
            base_url = self._base_url

        if version is None:
            version = self._version

        assert model is not None

        query = "?"
        for key, value in kwargs.items():
            query += "{}={}&".format(key, value)
        if query == "?":
            query = ""

        url = "{base_url}/api/{version}/{model}{query}".format(base_url=base_url, version=version, model=model, query=query)
        return url

    def post(self, url, data):

        response = requests.post(url, data=data, headers={
            "Authorization": self._api_token
        })
        print(response.text)
        #requests.post(url, data)