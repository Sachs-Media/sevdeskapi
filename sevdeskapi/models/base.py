from typing import TYPE_CHECKING

import sevdeskapi.exception as exception
import sevdeskapi.utils.map  as maputil

if TYPE_CHECKING:
    from sevdeskapi.controller.base import BaseController


class AbstractBaseModel:

    CONTROLLER_CLASS = None
    STRUCTURE = []


class BaseModel(maputil.AttributeMixin, AbstractBaseModel):

    def __init__(self, **kwargs):

        if not self.__class__.CONTROLLER_CLASS:
            raise RuntimeError("Every model must defined a CONTROLLER; this is no fault of yours, but the fault of the libary developer ")
        self.controller = self.__class__.CONTROLLER_CLASS(self)

        self._options = kwargs.pop("options", self.get_options())
        self._sevdesk_client = self._options.get("sevdesk_client")

        self.map_attributes(kwargs)

    def get_structure(self):
        return self.__class__.STRUCTURE

    def get_sevdesk_client(self):
        if not self._sevdesk_client:
            raise exception.NotConnectedToClient("Please link this to SevDeskClient object. Using client.send(<thisobject>) ")
        return self._sevdesk_client

    def use_sevclient(self, sevclient):

        if self._sevdesk_client is None:
            self._sevdesk_client = sevclient
        else:
            raise exception.AlreadyConnected("Another SevDeskClient is linked to this Model")

    @staticmethod
    def convert(self, sevdesk_client, field, data):
        """
        This method should be used by SevdeskTranslate to Convert a attribute to a submodal
        :return:
        """

        raise NotImplemented("This method is currently not implemented")

    def get_options(self):
        return {}

    def get_dict(self):
        data = {}
        for key, field in self.structure.items():
            if hasattr(self, field.name):
                data[field.apiname()] = getattr(self, field.name)
            elif field.required() and not hasattr(self, field.name):
                raise ValueError("The parameter {} is required".format(field.name))

        return data