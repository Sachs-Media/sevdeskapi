import sevdeskapi.controller.base as basecontroller
import urllib.parse


class TagController(basecontroller.BaseController):

    api_model = "Tag"

    def create(self, *args, **kwargs):
        request_url = self.get_sevdesk_client().build_url(model=self.get_apimodel_name())
        data = self.model.get_dict()
        data.update(kwargs)
        query = urllib.parse.urlencode(data)
        response = self.get_sevdesk_client().post("{}?{}".format(request_url, query))
        self.model.map_attributes(response["objects"])
        return response
