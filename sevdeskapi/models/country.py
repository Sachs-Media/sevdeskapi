import sevdeskapi.controller.country as country
from sevdeskapi.models.base import BaseModel
from sevdeskapi.utils.converter import Convert
from sevdeskapi.utils.sevdeskfield import SevDeskField


class Country(BaseModel):
    DEFAULT_OBJECT_NAME = "StaticCountry"
    CONTROLLER_CLASS = country.CountryController
    STRUCTURE = (
        SevDeskField("id", "id", ["country[id]"], converter=Convert.to_int),
        SevDeskField("objectName", "objectName", ["country[objectName]"]),
        SevDeskField("code", "code"),
        SevDeskField("name", "name"),
        SevDeskField("nameEn", "nameEn"),
        SevDeskField("translationCode", "translationCode"),
    )

    @staticmethod
    def convert(sevdesk_client, data, field, key):

        values = {}

        if "country" in data:

            if isinstance(data.get("country"), Country):
                values.update(data.get("country").get_dict())


            elif type(data.get("country")) is dict:
                values.update(data.get("country"))

        for item in [("id", "country[id]"), ("objectName", "country[objectName]")]:
            d = data.get(item[1])
            if d is not None:
                values[item[0]] = d

        model = Country(options={"sevdesk_client":sevdesk_client})

        model.map_attributes(values)

        return ("country", model)
