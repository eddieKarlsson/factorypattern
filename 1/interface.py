from abc import ABCMeta, abstractstaticmethod


class ICompany(metaclass=ABCMeta):

    @abstractstaticmethod
    def corp_method():
        """ Interface method """
