from sevdeskapi.controller.contact import ContactController
from sevdeskapi.models.category import Category
from sevdeskapi.models.base import BaseModel
from sevdeskapi.utils.sevdeskfield import SevDeskField


class Contact(BaseModel):

    CONTROLLER_CLASS = ContactController

    STRUCTURE = (
        SevDeskField("familyName", "familyname", filterable=True),
        SevDeskField("sureName", "surename", ["name2"]),
        SevDeskField("titel", "titel", ["academicTitle", "titel", "title"]),
        SevDeskField("description", "description"),
        SevDeskField("gender", "gender"),
        SevDeskField("customerNumber", "customerNumber"),
        SevDeskField("categoryId", "category[id]", converter=Category.convert, related_to="category"),
        SevDeskField("categoryObjectName", "category[objectName]", converter=Category.convert, related_to="category"),
        SevDeskField("category", "category", converter=Category.convert, nested=True),
    )
