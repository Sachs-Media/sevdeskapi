from sevdeskapi.utils.converter import Convert


class SevDeskTranslate:

    def __init__(self, name, apiname, aliases=[], converter=Convert.to_string):
        self._name = name # Name who set as Attribute at object
        self._apiname = apiname # NAme who used for communication with SevDesk
        self._aliases = aliases # other names that may come up
        self._converter = converter # Method who manage the datatype of field. Can be also a other Model

    def name(self):
        return self._name

    def apiname(self):
        return self._apiname

    def aliases(self):
        return self._aliases

    def converter(self, value, key, otherdata):
        return self._converter(value, key, otherdata)