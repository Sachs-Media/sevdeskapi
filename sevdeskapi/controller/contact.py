import sevdeskapi.controller.base as basecontroller


class ContactController(basecontroller.BaseController):

    api_model = "Contact"

    def create(self):

        customer_number = self.factory.getNextCustomerNumber()

        self.model.customerNumber = customer_number
        self.model.objectName = "Contact"
        # self.model.categoryId = 43
        # self.model.categoryObjectName = "Category"

        request_url = self.get_sevdesk_client().build_url(model=self.get_apimodel_name())
        data = self.model.get_dict()
        response = self.get_sevdesk_client().post(request_url, data)

        self.model.map_attributes(response.get("objects"))

        return response




    class Factory(basecontroller.BaseFactory):

        def getNextCustomerNumber(self):
            request_url = self.get_sevdesk_client().build_url(model=(self.controller.get_apimodel_name(), "Factory", "getNextCustomerNumber"))
            response = self.get_sevdesk_client().get(request_url)
            return response["objects"]