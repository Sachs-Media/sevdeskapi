class AttributeMixin(object):

    def _find_structure_field(self, needle):
        for key, value in self.structure().items():
            if needle in value.aliases() or \
               needle == value.name() or \
               needle == value.apiname():
                return value