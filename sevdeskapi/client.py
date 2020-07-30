

class SevDeskClient:
    """
        Initialize a Client who manage the Connections to the SevDesk API Endpoint
    """

    def __init__(self, api_token=None, base_url="https://my.sevdesk.de", version="v1"):
        assert api_token is not None

        self._api_token = api_token
        self._base_url = base_url
        self._version = version
