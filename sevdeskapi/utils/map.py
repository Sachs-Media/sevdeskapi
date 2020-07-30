class AttributeMixin(object):
    """
        Mixin for helper methods for working with Object attributes
    """

    def _find_structure_field(self, needle):
        """
            Helper method to find a "needle" in STRUCTURE.
            This method try to match needle with field (key), one of field aliases field.apiname or field.name

            :param needle: word/attribute which should be found in structure
            :return:
        """
        for key, value in self.structure().items():
            if needle in value.aliases() or \
               needle == value.name() or \
               needle == value.apiname():
                return value