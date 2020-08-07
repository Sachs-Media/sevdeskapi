import sevdeskapi.controller.document as documentcontroller
from sevdeskapi.models.base import BaseModel


class Document(BaseModel):
    CONTROLLER_CLASS = documentcontroller.DocumentController
    DEFAULT_OBJECT_NAME = "Document"
    STRUCTURE = (
    )