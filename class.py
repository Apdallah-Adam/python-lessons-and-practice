#              claass and method
class car:

    def swim(self):
        print("the shark is swiming")
    
    def dooli(self):
        print("doliga wa dilay!")


car = car()
car.swim()
car.dooli()


#                    NB

class car:

    def __init__(self, name,):
        self.name = name
    
    def swim(self):
        print(f"{self.name} is swiming")

    def shark(self):
        print(f"{self.name} is sharking")

abdall = car("cali")
abdall.swim()

abdi = car("hussein") 

abdi.shark()


#                         NB

class school:
    
    def __init__(self):
        print("in school class")


    def primery(self):
        print("primery school class")
    
    def secndery(self):
        print("secondery school class")


class course():

    def math(self):
        print("math course class")

    def engilish(sef):
        print("engilish course class")



class student(school , course):

    def __init__(self):
        print("in student class")


 
    def name(self):
        super().engilish()
        print("my name is abdalla")

std = student()

std.name()


#                   Polymorphism with  a class 

class cat:

    def color(self):
        print("white color")


    def legs(self):
        print(" 4 legs")


class humman:

    def color(self):
        print("whte , brown , blue")

    def legs(self):
        print(" 2 legs ")

c = cat()
h = humman()

for animal in (c , h):
    animal.color()
    animal.legs()


#                        Polymorphism with a function 


print(len('somalia'))
print(len(["python" , "java" , "PHP" ]))
print(len({"name : abdalla" , "address : mugadisho "}))



#  practice of class method

class bank:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} is deposied ${amount} ")

    def with_drow(self , amount):

        if amount < self.balance:
            self.balance -= amount
            print(f"{self.name} is with_drowed ${amount} ")
        else:
            print("invalid amoount try again!")

    def show_balance(self):
        print(f"the real amount is ${self.balance}")

account = bank("abadalla" , 100)
account.deposit(1)
account.show_balance()


account.with_drow(2)
account.show_balance()


#  car company

class car_company:

    def __init__(self,cars,balance):
        self.cars = cars
        self.balance = balance

    def sell_cars(self):
        print("choose any car you want")
        print("1. TAYOTO")
        print("2. CAROLE")
        print("3. CARIB")

choice = input("choose one of them: ")

car = car_company()
car.sell_cars()


#  

# # class Student:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def display(self):
# #         print(f"Student Name: {self.name}")
# #         print(f"Student Age: {self.age}")

# # # Get user input
# # name = input("Enter student's name: ")
# # age = input("Enter student's age: ")

# # # Create an object of the class
# # student1 = Student(name, age)

# # Display the student info
# student1.display()

        
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# # List to store all students
# students = []

# # Menu loop
# while True:
#     print("\n--- Student Menu ---")
#     print("1. Add new student")
#     print("2. Show all students")
#     print("3. Exit")

#     choice = input("Enter your choice (1-3): ")

#     if choice == "1":
#         name = input("Enter student name: ")
#         age = input("Enter student age: ")
#         student = Student(name, age)
#         students.append(student)
#         print("Student added successfully!")

#     elif choice == "2":
#         if not students:
#             print("No students yet.")
#         else:
#             print("\nList of Students:")
#             for i, s in enumerate(students, start=1):
#                 print(f"{i}. ", end="")
#                 s.display()

#     elif choice == "3":
#         print("Exiting program.")
#         break

#     else:
#         print("Invalid choice. Try again.")




# class students:
#     def __init__(self,name , age):
#         self.name = name 
#         self.age = age

#     def display(self):
#         print(f"name: {self.name} , age : {self.age}")


    
# students =[]
# while True:
#         print("\n---list of students---")
#         print("1. add new student")
#         print("2. show the stuents")
#         print("3. EXITS")

#         choice = input ("choice ne of this (1-3): ")

#         if choice == "1":
#             name=input("enter name: ")
#             age=input("enter age: ")
#             # student= student(name,age)
#             students.append(students)
#             print(f"\nstudent {name} added seccessful")

#         elif choice == "2":
#              if not students:
#                   print("\n there is no student ")
#              else:
#                   for i, s in enumerate(students ,start=1):
#                        print(f"{i}.",end="")
#                        students.display()






            
        