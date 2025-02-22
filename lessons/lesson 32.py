class TriangleChecker:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def check(self):
        print(c,'is c')
        if self.a < 0 or  self.b < 0 or self.c < 0:
            print("відємні числа не приймаються")
        else:
            if self.a + self.b > self.c and self.c + self.a > self.b and self.c + self.b > self.a:
                print("Такий трикутник ісснує")
            else:
                print("шкода, такий трикутник не існує")

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))


triangle = TriangleChecker(a,b,c)
triangle.c=-5
triangle.check()
print(triangle.c)














































