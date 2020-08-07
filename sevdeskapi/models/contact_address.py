import sevdeskapi.controller.contact_address as contactaddress
from sevdeskapi.models.base import BaseModel
from sevdeskapi.models import Contact, Country, Category
from sevdeskapi.utils.sevdeskfield import SevDeskField
from sevdeskapi.utils.converter import Convert
import enum


class ContactAddress(BaseModel):
    CONTROLLER_CLASS = contactaddress.ContactAddressController
    DEFAULT_OBJECT_NAME = "ContactAddress"
    STRUCTURE = (
        SevDeskField("contactId", "contact[id]", converter=Convert.to_int, filterable=True, related_to="contact"),
        SevDeskField("contactObjectName", "contact[objectName]", related_to="contact"),
        SevDeskField("contact", "contact", converter=Contact.convert, nested=True),
        SevDeskField("street", "street"),
        SevDeskField("zip", "zip", ["postal_code"], converter=Convert.to_int),
        SevDeskField("city", "city"),
        SevDeskField("countryId", "country[id]", related_to="country"),
        SevDeskField("countryObjectName", "country[objectName]", related_to="country"),
        SevDeskField("country", "country", converter=Country.convert, nested=True),
        SevDeskField("categoryId", "category[id]", filterable=True, related_to="category"),
        SevDeskField("categoryObjectName", "category[objectName]", filterable=True, related_to="category"),
        SevDeskField("category", "category", converter=Category.convert, nested=True),
        SevDeskField("objectName", "key[objectName]"),
    )
