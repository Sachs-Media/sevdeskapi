import sevdeskapi.controller.communication_way as communicationway
from sevdeskapi.models.base import BaseModel
from sevdeskapi.models.contact import Contact
from sevdeskapi.utils.sevdeskfield import SevDeskField
from sevdeskapi.utils.converter import Convert
import enum


class CommunicationWayType(enum.Enum):
    """
        Possibilitys of Communication Ways
    """
    PHONE = "PHONE"
    EMAIL = "EMAIL"


class CommunicationWay(BaseModel):
    CONTROLLER_CLASS = communicationway.CommunicationWayController
    DEFAULT_OBJECT_NAME = "CommunicationWay"
    STRUCTURE = (
        SevDeskField("contactId", "contact[id]", converter=Convert.to_int, filterable=True, related_to="contact"),
        SevDeskField("contactObjectName", "contact[objectName]", related_to="contact"),
        SevDeskField("contact", "contact", converter=Contact.convert, nested=True),
        SevDeskField("type", "type", filterable=True),
        SevDeskField("value", "value", filterable=True),
        SevDeskField("keyId", "key[id]", filterable=True),
        SevDeskField("keyObjectName", "key[objectName]", filterable=True),
        SevDeskField("objectName", "objectName", filterable=True),
    )