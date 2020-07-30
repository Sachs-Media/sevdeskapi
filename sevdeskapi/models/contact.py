from sevdeskapi.models.base import BaseModel
import sevdeskapi.controller.contact as contactcontroller


class Contact(BaseModel):
    CONTROLLER_CLASS = contactcontroller.ContactController
    pass