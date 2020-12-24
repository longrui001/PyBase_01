class _const:
    class ConstError(TypeError):pass
    class ConstCaseError(ConstError):pass

    def __setattr__(self,name,value):
        if self.__dict__.__contains__(name):
            raise self.ConstError("Can't change const.{}".format(name))
        if not name.isupper():
            raise self.ConstCaseError("const  {} is not all upercase".format(name))
        self.__dict__[name] = value


import sys
sys.modules[__name__] = _const()