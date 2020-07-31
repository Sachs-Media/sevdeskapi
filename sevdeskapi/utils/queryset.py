class Queryset:

    def __init__(self, model, *args):
        self._model = model

        for item in args:
            if not isinstance(item, self._model):
                raise ValueError("A Queryset can only contain objects from same model.")

        self._model_list = args

    def __iter__(self):
        for x in self._model_list:
            yield x

    def all(self):
        return self._model_list