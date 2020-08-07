import logging

log = logging.getLogger("sevdeskapi.utils")


class AttributeMixin(object):
    """
        Mixin for helper methods for working with Object attributes
    """

    def find_structure_field(self, needle):
        """
            Helper method to find a "needle" in STRUCTURE.
            This method try to match needle with field (key), one of field aliases field.apiname or field.name

            :param needle: word/attribute which should be found in structure
            :return:
        """
        for field in self.get_structure():

            if needle in field.aliases or \
               needle == field.name or \
               needle == field.apiname:
                return field

    def map_attributes(self, data):
        for key, item in data.items():
            field = self.find_structure_field(key)
            if field is None:
                log.debug("Attribute Mapping: Ignore parameter '{}'".format(key))
            else:
                converted_information = field.converter(self.get_sevdesk_client, data, field, key)
                setattr(self, *converted_information)