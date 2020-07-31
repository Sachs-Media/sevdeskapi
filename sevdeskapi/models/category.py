import sevdeskapi.controller.category as categorycontroller
import sevdeskapi.models.base as basemodel
from sevdeskapi.utils.sevdesktranslate import SevDeskTranslate


class Category(basemodel.BaseModel):
    CONTROLLER_CLASS = categorycontroller.CategoryController
    STRUCTURE = (
        SevDeskTranslate("id", "id", filterable=True),
        SevDeskTranslate("name", "name"),
        SevDeskTranslate("objectType", "objectType", filterable=True),
    )

    @staticmethod
    def convert(sevdesk_client, field, data):
        print("ASDFASDF")
        values = {}
        if "category" in data:
            values.update(data.get("category"))

        values["id"] = values.get("category[id]")
        values["name"] = values.get("category[name]")
        values["objectName"] = values.get("category[objectName]")
        model = Category(options={"sevdesk_client":sevdesk_client})
        model.map_attributes(values)
        print("-"*100)
        return ("category", model)
