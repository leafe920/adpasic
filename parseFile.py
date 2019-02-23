class Word:
    chineseName = ''
    englisthName
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def prt(self):
        print(self)
        print(self.__class__)
