import math


# Task 1
# class Shape:

#     def get_shape_area(self):
#         pass

    
# class Triangle(Shape):

#     def __init__(self, base, height):
#         self.base = base
#         self.height = height


#     def get_shape_area(self):
#         area_triangle = (self.base * self.height)//2
        
#         return (f"The area of triangle is {area_triangle}")
    

# class Square(Shape):
    
#     def __init__(self, length):
#         self.length = length

    
#     def get_shape_area(self):
#         area_square = self.length * self.length
        
#         return (f"The area of square is {area_square}")

# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     def get_shape_area(self):
#         pi = math.pi
#         area_circle = pi * (self.radius ** 2)
       
#         return (f"The area of circle is {area_circle}")




# triangle = Triangle(12, 5)
# print(triangle.get_shape_area())

# circle = Circle(3)
# print(circle.get_shape_area())

# square = Square(4)
# print(square.get_shape_area())


# Task 2

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname


    

#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.surname}")



# class Employee(Person):

#     def __init__(self, name, age, company, position):
#         super().__init__(name, age)
#         self.company = company
#         self.position = position

#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.surname}, я работаю в компании {self.company} на должности {self.position}.")



# class Student(Person):

#     def __init__(self, name, age, university, course):
#         super().__init__(name, age)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.surname}, я учусь в {self.university} на {self.course} курсе.")


# people = [
#     Person("Иван", "Петров"), 
#     Employee("Иван", "Петров", "Google", "программиста" ),
#     Student("Иван", "Петров", "MIT", "3")
#     ]

# for person in people:
#     person.get_info()
#     print()



# Task 3

/
