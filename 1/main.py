from factory import CompanyFactory

if __name__ == '__main__':
    while True:
        requested_company = input("write company code: ")
        corp = CompanyFactory.get_company(requested_company)
        corp.corp_method()
        print(f"corp class = {corp}, requested corp = {requested_company}")
        print(type(corp))
