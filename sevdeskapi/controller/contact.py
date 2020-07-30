import sevdeskapi.controller.base as basecontroller


class ContactController(basecontroller.BaseController):

    api_model = "Contact"

    def create(self):

        customer_number = self.factory().getNextCustomerNumber()

        self.model().customerNumber = customer_number
        self.model().objectName = "Contact"
        self.model().categoryId = 43
        self.model().categoryObjectName = "Category"

        request_url = self.sevdesk_client().build_url(model=self.apimodel())
        data = self.model().get_dict()
        response = self.sevdesk_client().post(request_url, data)
        print(response)


    class Factory(basecontroller.BaseFactory):

        def getNextCustomerNumber(self):
            request_url = self.sevdesk_client().build_url(model=(self.controller().apimodel(), "Factory", "getNextCustomerNumber"))
            response = self.sevdesk_client().get(request_url)
            return response["objects"]