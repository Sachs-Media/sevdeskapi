from sevdeskapi.exception import NotConnectedToClient


class BaseModel:

    CONTROLLER_CLASS = None

    def __init__(self, sevdesk_client=None):
        if not self.__class__.CONTROLLER_CLASS:
            raise RuntimeError("Every model must defined a CONTROLLER; this is no fault of yours, but the fault of the libary developer ")
        self._sevdesk_client = sevdesk_client

        self._controller = self.__class__.CONTROLLER_CLASS(self)

    def sevdesk_client(self):
        if not self._sevdesk_client:
            raise NotConnectedToClient("Please link this to SevDeskClient object. Using client.send(<thisobject>) ")
        return self._sevdesk_client