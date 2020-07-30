from sevdeskapi.exception import NotConnectedToClient


class BaseController:

    def __init__(self, model):
        self._model = model

    def sevdesk_client(self):
        if not self.model._sevdesk_client:
            raise NotConnectedToClient("Please link this to SevDeskClient object. Using client.send(<thisobject>) ")
        return self.model._sevdesk_client