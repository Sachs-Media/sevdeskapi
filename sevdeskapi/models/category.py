import sevdeskapi.controller.contact as contactcontroller
import sevdeskapi.models.base as basemodel
from sevdeskapi.utils.sevdesktranslate import SevDeskTranslate


class Category(basemodel.BaseModel):
    CONTROLLER_CLASS = contactcontroller.CategoryController
    STRUCTURE = {
        "familyname": SevDeskTranslate("familyName", "familyname"),
        "surename": SevDeskTranslate("sureName", "surename", ["name2"]),
        "title": SevDeskTranslate("title", "title", ["academicTitle", "title"]),
        "description": SevDeskTranslate("description", "description"),
        "gender": SevDeskTranslate("gender", "gender"),
        "customerNumber": SevDeskTranslate("customerNumber", "customerNumber"),
        "category[id]": SevDeskTranslate("categoryId", "category[id]"),
        "category[objectName]": SevDeskTranslate("categoryObjectName", "category[objectName]")
    }
