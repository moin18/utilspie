

class frozendict(dict):
    """
    Hashable and immutable dict object

    For example:
    frozendict_object = frozendict({1: 2, 3: 4})
    """
    def __key(self):
        return tuple((key, self[key]) for key in sorted(self))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __repr__(self):
        return '{}({})'.format(type(self).__name__, super(type(self), self).__repr__())

    def update(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.update.__name__, type(self).__name__))

    def pop(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.pop.__name__, type(self).__name__))

    def popitem(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.popitem.__name__, type(self).__name__))

    def setdefault(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.setdefault.__name__, type(self).__name__))

    def clear(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.clear.__name__, type(self).__name__))

    def __setitem__(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.__setitem__.__name__, type(self).__name__))

    def __setattr__(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.__setattr__.__name__, type(self).__name__))

    def __delitem__(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.__delitem__.__name__, type(self).__name__))

    def __delattr__(self, *args, **kwargs):
        raise AttributeError("You can not call '{}()' for '{}' object".format(
            self.__delattr__.__name__, type(self).__name__))
