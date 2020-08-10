import requests
import sevdeskapi.models

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
            model.controller.create()

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

        if type(model) in [list, tuple]:
            model = "/".join(model)

        query = "?"
        for key, value in kwargs.items():
            query += "{}={}&".format(key, value)
        if query == "?":
            query = ""

        url = "{base_url}/api/{version}/{model}{query}".format(base_url=base_url, version=version, model=model, query=query)
        return url

    def _default_header(self):
        return {
            "Authorization": self._api_token
        }

    def post(self, url, data=None, files=None, headers=None):

        header = self._default_header()

        if headers is not None:
            header.update(headers)

        response = requests.post(url, data=data, headers=header, files=files)

        if 299 <= response.status_code >= 200:
            print(data)
            print(response.json())
            raise ValueError("This is not a valid request. Statuscode %s" % str(response.status_code))

        return response.json()

    def get(self, url):

        response = requests.get(url, headers={
            "Authorization": self._api_token
        })

        if 299 <= response.status_code >= 200:
            raise ValueError("This is not a valid request. Statuscode %s" % str(response.status_code))

        return response.json()

    def controller(self):
        return SevDeskClient.Controller(self)

    class Controller:

        def __init__(self, client):
            self.category = sevdeskapi.models.Category(options={"sevdesk_client": client}).controller
            self.contact = sevdeskapi.models.Contact(options={"sevdesk_client": client}).controller
            self.tag = sevdeskapi.models.Tag(options={"sevdesk_client": client}).controller
            self.communicationWay = sevdeskapi.models.CommunicationWay(options={"sevdesk_client": client}).controller
            self.country = sevdeskapi.models.Country(options={"sevdesk_client": client}).controller
            self.feed = sevdeskapi.models.Feed(options={"sevdesk_client": client}).controller
            self.contactAddress = sevdeskapi.models.ContactAddress(options={"sevdesk_client": client}).controller