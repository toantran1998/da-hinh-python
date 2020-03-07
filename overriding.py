class Parent():
    def __init__(self):
        self.value = "Day la lop cha"
    def show(self):
        print(self.value)
class Child(Parent):
    def __init__(self):
        self.value = "day la lop con duoc ke thua tu lop cha"
    def show(self):
        print(self.value)
cha = Parent()
con = Child()

cha.show()
con.show()