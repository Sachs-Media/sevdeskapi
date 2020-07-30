import sevdeskapi.controller.base as basecontroller


class ContactController(basecontroller.BaseController):

    api_model = "Contact"

    def create(self):
        request_url = self.sevdesk_client().build_url(model=self.apimodel())

        self.sevdesk_client().post(request_url, self.model().get_dict())

        pass

