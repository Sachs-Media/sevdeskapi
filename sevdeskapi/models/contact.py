from sevdeskapi.models.base import BaseModel
import sevdeskapi.controller.contact as contactcontroller
from sevdeskapi.utils.sevdesktranslate import SevDeskTranslate


class Contact(BaseModel):
    CONTROLLER_CLASS = contactcontroller.ContactController
    STRUCTURE = {
        "familyname": SevDeskTranslate("familyName", "familyname"),
        "surename": SevDeskTranslate("sureName", "surename"),
        "title": SevDeskTranslate("title", "title"),
        "description": SevDeskTranslate("description", "description"),
        "gender": SevDeskTranslate("gender", "gender"),
    }

    def __init__(self, **kwargs):
        self._options = kwargs.pop("options", self.get_options())
        self.mapattributes(kwargs)
        pass


