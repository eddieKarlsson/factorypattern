from corps.mc import mc
from corps.tp import tp


class CompanyFactory:

    @staticmethod
    def get_company(company_type):
        try:
            if company_type == 'mc':
                return mc()
            if company_type == 'tp':
                return tp()
            raise AssertionError("Error: type not found")
        except AssertionError as _e:
            print(_e)
