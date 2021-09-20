from interface import ICompany


class tp(ICompany):
    def __init__(self):
        self.name = 'tp'

    def corp_method(self):
        print(f"I am tp, my identity is {self.name}")
