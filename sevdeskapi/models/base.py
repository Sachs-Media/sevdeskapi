from sevdeskapi.exception import NotConnectedToClient
from sevdeskapi.utils.map import AttributeMixin


class AbstractBaseModel:

    CONTROLLER_CLASS = None
    STRUCTURE = {}

    def structure(self):
        return self.__class__.STRUCTURE

    def controller_class(self):
        return self.__class__.CONTROLLER_CLASS


class BaseModel(AttributeMixin, AbstractBaseModel):

    def __init__(self, sevdesk_client=None):
        if not self.controller_class():
            raise RuntimeError("Every model must defined a CONTROLLER; this is no fault of yours, but the fault of the libary developer ")
        self._controller = self.controller_class()(self)
        self._sevdesk_client = sevdesk_client

    def sevdesk_client(self):
        if not self._sevdesk_client:
            raise NotConnectedToClient("Please link this to SevDeskClient object. Using client.send(<thisobject>) ")
        return self._sevdesk_client

    def mapattributes(self, data):

        for key, item in data.items():

            field = self._find_structure_field(key)
            setattr(self, field.name(), field.converter(item, key, data))


    def convert(self):
        """
        This method should be used by SevdeskTranslate to Convert a attribute to a submodal
        :return:
        """
        raise NotImplemented("This method is currently not implemented")


    def get_options(self):
        return {}