from interface import ICompany


class mc(ICompany):
    def __init__(self):
        self.name = 'mc'

    def corp_method(self):
        print(f"I am mc, my identity is {self.name}")
