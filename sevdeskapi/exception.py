class NotConnectedToClient(AttributeError):
    """
        Raises when a method of the model object is called without a reference to SevDeskClient
    """
    pass


class AlreadyConnected(ValueError):
    """
        Raises when a model was tryed to referenced second time to a sevdeskclient

    """
    pass


class NonFilterableParameter(ValueError):
    """
        This error rais when find is used with an  disallowed (not filterable) parameter
    """
    pass