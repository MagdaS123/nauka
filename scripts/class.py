class MyFirstClass():
    variable1 = 1
    variable2 = 2
    def function(self):
        print("Hello world")

object = MyFirstClass()
object.variable1
print(object.variable1)

object2 = MyFirstClass()
object2.variable2
print(object2.variable2)

object3 = MyFirstClass
object3.function(self)
print(object3.function(self))