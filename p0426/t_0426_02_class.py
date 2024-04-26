class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        # 맴버 변수 선언이 불필요
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result


a = FourCal(10, 20)
print(type(a))
a.setdata(10, 20)
print(a.add())



