from typing import TYPE_CHECKING
import logging
import sevdeskapi.exception as exception

if TYPE_CHECKING:
    from sevdeskapi.models.base import BaseModel
    from sevdeskapi.client import SevDeskClient


log = logging.getLogger("basemodel")


class BaseController:
    """
        This class manages the datastructures and URLs for a Model
    """

    def __init__(self, model):
        """
            Constructor. adds model as Attribute

            :param model: The model who use this controller
            :type model: BaseModel
        """
        self.model = model

        if hasattr(self, "Factory"):
            self.factory = self.__class__.Factory(self)

    def get_sevdesk_client(self) -> "SevDeskClient":
        """
            Getter for deliver the SevDeskClient object

            :return SevDeskClient:
        """

        if not self.model.get_sevdesk_client():
            raise exception.NotConnectedToClient("Please link this to SevDeskClient object. Using client.send(<thisobject>) ")
        return self.model.get_sevdesk_client()

    def get_apimodel_name(self) -> str:
        """
            Returns the name of API Endpoint (model) BaseURL + Controller + Version + Model: https://my.sevdesk.de/api/v1/Contact/

            :return str: Mmodel-name
        """
        return self.__class__.api_model

    def create(self, *args, **kwargs):
        """
            Creates a new Object at API
            by default it uses the linked model for informations.
            Yo can overwrite the request parameters it via kwargs

            :param kwargs: Arguments which should be overwritten

            :return request: The orginal requests response
        """
        request_url = self.get_sevdesk_client().build_url(model=self.get_apimodel_name())
        data = self.model.get_dict()
        data.update(kwargs)
        response = self.get_sevdesk_client().post(request_url, data)
        self.model.map_attributes(response["objects"])

        return response

    def find(self, **kwargs):
        """
            Find a Object which matches by given kwargs

            :param kwargs: Search Query (names defined at Model.Structure
            :return BaseModel: Model object from the found object
        """
        search_parameter = {}
        for key, value in kwargs.items():
            field = self.model.find_structure_field(key)
            if field.filterable:
                search_parameter[field.apiname] = value
            else:
                raise exception.NonFilterableParameter("Its not allowed to filter by '{}'".format(key))
        request_url = self.get_sevdesk_client().build_url(model=self.get_apimodel_name(), **search_parameter)
        print(request_url)
        response = self.get_sevdesk_client().get(request_url)
        model_list = []
        for item in response["objects"]:
            model = self.model.__class__(options={"sevdesk_client": self.get_sevdesk_client()})
            model.map_attributes(item)
            model_list.append(model)

        return model_list

    def get_or_create(self, **kwargs):
        """
            Searches a Value, if no result creates a new one with the same
            Values

            :return tuple(object: BaseModel, created: bool): object contains the (existing) api object, created is a boolean if the data
            was new created or already exist
        """
        result = self.find(**kwargs)
        if len(result) <= 0:
            self.create(**kwargs)
            created = True
        elif len(result) > 1:
            log.info([ item.name for item in result ])
            raise ValueError("too many results")
        else:
            self.model.map_attributes(result[0].get_dict())
            created = False

        return self.model, created


class BaseFactory:

    def __init__(self, controller):
        self.controller = controller

    def get_sevdesk_client(self):
        return self.controller.get_sevdesk_client()
