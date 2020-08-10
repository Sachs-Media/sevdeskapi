import sevdeskapi.controller.country as country
from sevdeskapi.models.base import BaseModel
from sevdeskapi.utils.converter import Convert
from sevdeskapi.utils.sevdeskfield import SevDeskField
import sevdeskapi.controller.tag as tagcontroller


class Tag(BaseModel):
    CONTROLLER_CLASS = tagcontroller.TagController
    STRUCTURE = (
        SevDeskField("id", "id", ["tag[id]"], converter=Convert.to_int, filterable=True),
        SevDeskField("name", "name", ["tag[name]"], filterable=True),
        SevDeskField("tagId", "tag[id]"),
        SevDeskField("objectName", "objectName", ["objectName", "tag[objectName]", "tagObjectName"]),
    )

    def relateTo(self, object):

        data = {
            "tag[id]": self.id,
            "tag[objectName]": self.objectName,
            "object[id]": object.id,
            "object[objectName]": object.objectName,

        }

        request_url = self.get_sevdesk_client().build_url(
            model="TagRelation")
        response = self.get_sevdesk_client().post(request_url, data)
        return response["objects"]