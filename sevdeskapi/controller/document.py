import sevdeskapi.controller.base as basecontroller
import urllib.parse

class DocumentController(basecontroller.BaseController):

    api_model = "Document"

    def create(self):
        raise NotImplemented("This method is currently not implemnted at this endpoint")

    class Factory(basecontroller.BaseFactory):

        def fileUpload(self, object, file):
            request_url = self.get_sevdesk_client().build_url(model=(self.controller.get_apimodel_name(), "Factory", "fileUpload"))

            query = urllib.parse.urlencode({
                "object[id]": object.id,
                "object[objectName]": object.objectName,
            })

            response = self.get_sevdesk_client().post("{}?{}".format(request_url, query), files={"files": (file.file_name, file.uploaded_file.open("rb"), file.content_type)})

            return response["objects"]