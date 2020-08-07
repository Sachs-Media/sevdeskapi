import sevdeskapi.controller.country as country
from sevdeskapi.models.base import BaseModel
from sevdeskapi.utils.converter import Convert
from sevdeskapi.utils.sevdeskfield import SevDeskField
import sevdeskapi.controller.feed as feedcontroller


class Feed(BaseModel):
    DEFAULT_OBJECT_NAME = "Feed"
    CONTROLLER_CLASS = feedcontroller.FeedController
    STRUCTURE = (
    )
