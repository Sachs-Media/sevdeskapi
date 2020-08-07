import sevdeskapi.controller.base as basecontroller
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import time

class FeedController(basecontroller.BaseController):

    api_model = "Feed"

    def create(self):
        raise NotImplemented("This method is not implemented for this Endpoint")


    class Factory(basecontroller.BaseFactory):

        def addNotice(self, text="", notify=None, object=None):

            if object is None:
                raise ValueError("Method-Argument 'object' is required")

            request_url = self.get_sevdesk_client().build_url(model=(self.controller.get_apimodel_name(), "Factory", "addNotice"))

            mp_encoded = MultipartEncoder(fields={
                "object[id]": str(object.id),
                "object[objectName]": str(object.objectName),
                "text": str(text),
                "date": str(int(time.time())),
                "notify": "null"
            })
            response = self.get_sevdesk_client().post(request_url,
                                                      data=mp_encoded.to_string(),
                                                      headers={'Content-Type': mp_encoded.content_type}
                                                      )
            return response