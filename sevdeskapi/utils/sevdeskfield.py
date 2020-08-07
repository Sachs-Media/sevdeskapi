from sevdeskapi.utils.converter import Convert
import logging

log = logging.getLogger("sevdeskapi.utils")


class SevDeskField:

    def __init__(self, name, apiname, aliases=None, related_to=None, converter=None, required=False, filterable=False, nested=False):
        if aliases is None:
            aliases = []
        if converter is None:
            converter = Convert.to_string

        self.name = name # Name who set as Attribute at object
        self.apiname = apiname # NAme who used for communication with SevDesk
        self.aliases = aliases # other names that may come up
        self.related_to = related_to # specifies a related field
        self.converter = converter # Method who manage the datatype of field. Can be also a other Model
        self.required = required # specifies whether the parameter is required for requets
        self.filterable = filterable # specifies if this parameter can be used as filter
        self.nested = nested # Is true when this field contains a nested model
