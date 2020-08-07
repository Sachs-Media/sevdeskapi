class Convert:
    """
        A very basic converter class
    """

    @staticmethod
    def to_string(get_sevdesk_client_method, data, field, key):
        """
            Converts input value to string

            :return:
        """
        return (field.name, str(data[key]))


    @staticmethod
    def to_int(get_sevdesk_client_method, data, field, key):
        """
            Converts input value to string

            :return:
        """
        return (field.name, int(data[key]))