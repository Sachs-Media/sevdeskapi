from typing import TYPE_CHECKING

import sevdeskapi.exception as exception

if TYPE_CHECKING:
    from sevdeskapi.models.base import BaseModel
    from sevdeskapi.client import SevDeskClient


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
        self._model = model

    def sevdesk_client(self) -> "SevDeskClient":
        """
            Getter for deliver the SevDeskClient object

            :return SevDeskClient:
        """

        if not self.model().sevdesk_client():
            raise exception.NotConnectedToClient("Please link this to SevDeskClient object. Using client.send(<thisobject>) ")
        return self.model().sevdesk_client()

    def model(self) -> "BaseModel":
        """
            Getter for Model who used this Controller

            :return BaseModel: Model who use this Controller inherith from BaseModel
        """
        return self._model

    def apimodel(self) -> str:
        """
            Returns the name of API Endpoint (model) BaseURL + Controller + Version + Model: https://my.sevdesk.de/api/v1/Contact/

            :return str: Mmodel-name
        """
        return self.__class__.api_model

    def create(self, *args, **kwargs):
        raise NotImplemented("This model doesnt have implement a create method")