import sevdeskapi.controller.category as categorycontroller
from sevdeskapi.models.base import BaseModel
from sevdeskapi.utils.sevdeskfield import SevDeskField
from sevdeskapi.utils.converter import Convert


class Category(BaseModel):
    CONTROLLER_CLASS = categorycontroller.CategoryController
    DEFAULT_OBJECT_NAME = "Category"
    STRUCTURE = (
        SevDeskField("id", "id", ["category[id]"], converter=Convert.to_int, filterable=True),
        SevDeskField("name", "name", ["category[name]"]),
        SevDeskField("objectType", "objectType", ["category[objectType]"], filterable=True),
        SevDeskField("objectName", "objectName", ["category[objectName]"], filterable=True),
    )

    @staticmethod
    def convert(sevdesk_client, data, field, key):

        values = {}
        if "category" in data:
            if isinstance(data.get("category"), Category):
                values.update(data.get("category").get_dict())
            elif type(data.get("category")) is dict:
                values.update(data.get("category"))

        for item in [("id", "category[id]"), ("name", "category[name]"), ("objectName", "category[objectName]")]:
            d = data.get(item[1])
            if d is not None:
                values[item[0]] = d

        model = Category(options={"sevdesk_client":sevdesk_client})
        model.map_attributes(values)
        return ("category", model)
