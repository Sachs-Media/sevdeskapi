from sevdeskapi.controller.contact import ContactController
from sevdeskapi.models.category import Category
from sevdeskapi.models.base import BaseModel
from sevdeskapi.utils.sevdeskfield import SevDeskField
import enum



class Contact(BaseModel):

    CONTROLLER_CLASS = ContactController

    STRUCTURE = (
        SevDeskField("id", "id", ["contact[id]"], filterable=True),
        SevDeskField("objectName", "objectName", ["contact[objectName]"], filterable=True),
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


    @staticmethod
    def convert(sevdesk_client, data, field, key):

        values = {}

        if "contact" in data:

            if isinstance(data.get("contact"), Contact):
                values.update(data.get("contact").get_dict())


            elif type(data.get("contact")) is dict:
                values.update(data.get("contact"))

        for item in [("id", "contact[id]"), ("objectName", "contact[objectName]")]:
            d = data.get(item[1])
            if d is not None:
                values[item[0]] = d

        model = Contact(options={"sevdesk_client":sevdesk_client})

        model.map_attributes(values)

        return ("contact", model)
