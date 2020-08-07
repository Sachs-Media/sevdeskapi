from typing import TYPE_CHECKING

import sevdeskapi.exception as exception
import sevdeskapi.utils.map as maputil

if TYPE_CHECKING:
    from sevdeskapi.controller.base import BaseController


class AbstractBaseModel:

    CONTROLLER_CLASS = None
    STRUCTURE = []
    DEFAULT_OBJECT_NAME = ""


class BaseModel(maputil.AttributeMixin, AbstractBaseModel):

    def __init__(self, **kwargs):

        if not self.__class__.CONTROLLER_CLASS:
            raise RuntimeError("Every model must defined a CONTROLLER; this is no fault of yours, but the fault of the libary developer ")
        self.controller = self.__class__.CONTROLLER_CLASS(self)

        self._options = kwargs.pop("options", self.get_options())

        self._sevdesk_client = self._options.get("sevdesk_client")
        if self.__class__.DEFAULT_OBJECT_NAME:
            self.objectName = self.__class__.DEFAULT_OBJECT_NAME

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
    def convert(sevdesk_client, data, field, key):
        """
        This method should be used by SevdeskTranslate to Convert a attribute to a submodal
        :return:
        """
        raise NotImplemented("This method is currently not implemented")

    def get_options(self):
        return {}

    def get_dict(self, data=None):
        """
            Returns current Model object as dict
            :return dict: dict representation of current object
        """

        if data is None:
            data = {}

        for field in self.get_structure():
            if hasattr(self, field.name):
                value = getattr(self, field.name)

                if field.nested:
                    # find fields which are related to the nested field
                    related_fields = list(filter(lambda item: item.related_to == field.name, self.get_structure()))
                    data.update(value.parent_update(data, related_fields))
                else:
                    data[field.apiname] = value

            elif field.required and not hasattr(self, field.name):
                raise ValueError("The parameter {} is required".format(field.name))

        return data

    def parent_update(self, data, remote_fields):
        new_data = {}
        for field in remote_fields:

            local_field_list = list(
                set(
                    filter(
                        lambda item: item is not None,
                        [
                            self.find_structure_field(field.apiname),
                            self.find_structure_field(field.name)
                        ] +
                        [
                            self.find_structure_field(alias) for alias in field.aliases
                        ]
                    )
                )
            )


            if len(local_field_list) > 1:
                raise ValueError("Multiple fields have the same alias, apiname or name")

            local_field = local_field_list[0]
            if hasattr(self, local_field.name):
                new_data[field.apiname] = getattr(self, local_field.name)

        return new_data