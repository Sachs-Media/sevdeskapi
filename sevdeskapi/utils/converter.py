class Convert:
    """
        A very basic converter class
    """

    @staticmethod
    def to_string(sevdesk_client, field, data):
        """
            Converts input value to string

            :return:
        """
        return (field.name, str(data[field.apiname]))