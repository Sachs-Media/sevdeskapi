from sevdeskapi.utils.converter import Convert
import logging

log = logging.getLogger("sevdeskapi.utils")


class SevDeskTranslate:

    def __init__(self, name, apiname, aliases=[], converter=Convert.to_string, required=False, filterable=False):
        self.name = name # Name who set as Attribute at object
        self.apiname = apiname # NAme who used for communication with SevDesk
        self.aliases = aliases # other names that may come up
        self.converter = converter # Method who manage the datatype of field. Can be also a other Model
        self.required = required # specifies whether the parameter is required for requets
        self.filterable = filterable # specifies if this parameter can be used as filter
