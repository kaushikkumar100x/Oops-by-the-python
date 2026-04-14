#class and object

#car showroom
# class car:
#     def __init__(self,name,color,year):
#         self.name = name
#         self.color = color
#         self.year = year
# c1 = car("BMW","black",2025) 
# print(c1.name,c1.color,c1.year)


#2nd type of car showroom
# class Car:
#     def __init__(self,name,color,year):
#         self.name = name
#         self.color =  color
#         self.year = year
#     def display_details(self):# diplay karne ka liye use kiya 
#         print(f"car name is {self.name}")
#         print(f"car color is {self.color}")
#         print(f"car year is {self.year}")
# c1 = Car("BMW","black",2025)
# c2 = Car("audi","white",2024)

# c1.display_details()
# print()
# c2.display_details()

# student management system
# class Student:
#     def __init__(self,name,age,Class,grade):
#         self.name = name 
#         self.age = age
#         self.Class = Class
#         self.grade = grade
# s1 = Student("kaushik",18,"12th",100)
# print(s1.name,s1.age,s1.Class,s1.grade)




#student management system with the help of display

# class Student:
#     def __init__ (self,name , age, marks,grade):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         self.grade =  grade
#     def Student_details(self):
#          print(f"student name is {self.name}")
#          print(f"student age is {self.age}")
#          print(f"student mark is {self.marks}")
#          print(f"student grade is {self.grade}")
         
         
# s1 = Student("kaushik",18,100,"A+")
# s1.Student_details()


# library management system
# class Book:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year
    
# b1 = Book("python programming","john smith",2020)
# print(b1.title,b1.author,b1.year)


# second type of with the help of display
# class Book:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def display_details(self):
#         print(f"book title is {self.title}")
#         print(f"book author is {self.author}")
#         print(f"book year is {self.year}")
        
# b1 = Book("python programming","john smith",2020)
# b1.display_details()

#bank account simulation with the help of display
# class BankAccount:
#     def __init__(self,account_number,account_holder,balance):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance
#     def display_details(self):
#         print(f"account number is {self.account_number}")
#         print(f"account holder is {self.account_holder}")
#         print(f"account balance is {self.balance}")
# b1 = BankAccount("123456789","kaushik",10000)
# b1.display_details()


#bank account simulation simple way
# class BankAccount:
#     def __init__(self,Account_number,Account_holder,balance):
#         self.Account_number = Account_number
#         self.Account_holder = Account_holder
#         self.balance = balance
# b1 =BankAccount("123456789","kaushik",10000)
# print(b1.Account_number,b1.Account_holder,b1.balance)

 #bank Accound Simulation withdrow and deposit
class BankAccount:
    def __init__(self,account_number,account_holder,balance):
         self.account_number = account_number
         self.account_holder = account_holder
         self.balance = balance 
    def deposit(self,amount):
        self.balance += amount
        print(f"deposit anount is{amount}")
        print(f"Current balance is {self.balance}")
    def withdrow(self,amount):
        if amount > self.balance:
            print("insufficient balance")
        elif amount <= self.balance:
            self.balance -=amount
            print(f"withdrow amount{amount}")
            print(f"current balance is {self.balance}")
        else:
            print("invalid amount")
        
b1 = BankAccount("123456789","kaushik",10000)
b1.deposit(5000)        
b1.withdrow(2000)
print(b1.account_number,b1.account_holder,b1.balance)
            