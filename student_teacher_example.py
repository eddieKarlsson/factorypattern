from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """ Interface method """


class mc(IPerson):
    def __init__(self):
        self.name = "mc - Name"

    def person_method(self):
        print("I am a mc", self.name)


class tp(IPerson):
    def __init__(self):
        self.name = "tp - Name"

    def person_method(self):
        print("I am a tp", self.name)


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        try:
            if company_type == 'mc':
                return(mc)
            if person_type == "tp":
                return tp()

            raise AssertionError("ERROR: type not found")
        except AssertionError as _e:
            print(_e)

        if person_type == "mc":
            return mc()
        print("Error: invalid type")
        return -1


if __name__ == '__main__':
    choice = input("what type: ")
    person = PersonFactory.build_person(choice)
    person.person_method()



# s1 = mc()
# s1.person_method()
#
# t1 = tp()
# t1.person_method()
