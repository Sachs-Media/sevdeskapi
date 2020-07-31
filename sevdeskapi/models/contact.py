import sevdeskapi.controller.contact as contactcontroller
import sevdeskapi.controller.category as categorycontroller
import sevdeskapi.models.category as categorymodels
import sevdeskapi.models.base as basemodel
from sevdeskapi.utils.sevdesktranslate import SevDeskTranslate


class Contact(basemodel.BaseModel):

    CONTROLLER_CLASS = contactcontroller.ContactController

    STRUCTURE = (
        SevDeskTranslate("familyName", "familyname", filterable=True),
        SevDeskTranslate("sureName", "surename", ["name2"]),
        SevDeskTranslate("titel", "titel", ["academicTitle", "titel", "title"]),
        SevDeskTranslate("description", "description"),
        SevDeskTranslate("gender", "gender"),
        SevDeskTranslate("customerNumber", "customerNumber"),
        SevDeskTranslate("categoryId", "category[id]", converter=categorymodels.Category.convert),
        SevDeskTranslate("categoryObjectName", "category[objectName]", converter=categorymodels.Category.convert),
        SevDeskTranslate("category", "category", converter=categorymodels.Category.convert),
    )
