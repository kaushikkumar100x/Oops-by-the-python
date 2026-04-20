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
# class BankAccount:
#     def __init__(self,account_number,account_holder,balance):
#          self.account_number = account_number
#          self.account_holder = account_holder
#          self.balance = balance 
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"deposit anount is{amount}")
#         print(f"Current balance is {self.balance}")
#     def withdrow(self,amount):
#         if amount > self.balance:
#             print("insufficient balance")
#         elif amount <= self.balance:
#             self.balance -=amount
#             print(f"withdrow amount{amount}")
#             print(f"current balance is {self.balance}")
#         else:
#             print("invalid amount")
            
#         @classmethod
#         def from_string(cls,account_string):
#             account_number,account_holder,balance = account_string.split(",")
#             return cls(account_number,account_holder,int(balance))
#         @staticmethod
#         def calculate_interste(balance ,rate ,time):
#               return balance *rate*time/100
          
        
# b1 = BankAccount("123456789","kaushik",10000)
# b1.deposit(5000)        
# b1.withdrow(2000)
# print(b1.account_number,b1.account_holder,b1.balance)




   

#=======================inheritance concepts ========================

#single inheritance : parent -> student

# class parent:
#     def skill(self):
#         print("programing skills")
# class student(parent):
#     def hobby(self):
#         print("reading book")
        
# s1 = student()
# s1.skill()
# s1.hobby()

    
            # ========================= multiple  inheritance : Animal-> cat -> dog
            
            
# class animal:
#     def eat(self):
#         print("its eating the food")
# class cat:
#     def mewo(self):
#         print("cat is mewoing")
# class dog:
#     def bow(self):
#         print("dog is bowing")  
# class pet(animal,cat,dog):
#     pass


# p1 = pet()
# p1.eat()
# p1.mewo()
# p1.bow()





#=================================multilevel inheritance father + mother -> child



# class grandfather:
#     def height(self):
#         print("grandfather is 6 feet tall")
# class father(grandfather):
#     def haircolor(self):
#         print("father has black hair")
# class son(father):
#     def eyescolor(self):
#         print("son has brown eyes")
        
        
# p1 = son()
# p1.height()
# p1.eyescolor()
# p1.haircolor()
    
    
    
    
    
    #=================================hierarchical inheritance father -> son1,son2
    
# class father:
#     def eat(self):
#         print("eating")
# class son1(father):
#     def eyescolor(self):
#         print("black")
# class son2(father):
#     def haircolor(self):
#         print("Brown")
        
        
        
# s1 = son1()
# s2 = son2()


# s1.eat()
# s2.eat()
# s1.eyescolor()
# s2.haircolor()






# ===============================hybrid inheritance father -> son1,son2 -> grandson


# class father:
#     def tall(self):
#         print("tall")
# class son1(father):
#     def haircolor(self):
#         print("black")  
# class son2(father):
#     def eyescolor(self):
#         print("brown")
# class grandson(son1,son2):
#     pass


# g1 = grandson()
# g1.tall()           
# g1.haircolor()
# g1.eyescolor()





#===================Super function ==============


# class animal:
#     def show(self):
#         print("eating")
# class dog(animal):
#     def show(self):
#         super().show() # super function is used to call the parent class method
#         print("barking")
# class cat(dog):
#     def show(self):
#         super().show() # super function is used to call the parent class method
#         print("walking")
    
    
    
# c1 = cat() 
# c1.show()



#========================Method overriding =====================


# class parent:
#     def skill(self):
#         print("manual works")
# class child(parent):
#     def skill(self):
#         print("digital works")


# c1 = child()
# c1.skill()






#==========================duck typing========================

 # =====================birds and kite  by fly() method  duck typing========================
 
# class birds:
#      def fly(self):
#          print("birds are fly on the sky")
# class kite:
#     def fly(self):
#         print("kite is flying in the sky:")
        
        
# def make_it_fly(obj):
#      obj.fly()
# b = birds()
# k = kite()
    
# make_it_fly(b)
# make_it_fly(k)



#================================multiplie inheritance  program = WAP two parent class as  name of width the display function subject and roll number=================

# class A:
#     def __init__(self, name , salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print(f"name is {self.name}")
#         print(f"salary is {self.salary}")
#         print("\n")

# s1 = A("kaushik",10000)
# s1.display()      


# class B:
#     def __init__(self, name , subject , Roll_no):
#         self.name = name
#         self.subject = subject
#         self.Roll_no = Roll_no
#     def display(self):
#         print(f"name is {self.name}")
#         print(f"subject is {self.subject}")
#         print(f"roll number is {self.Roll_no}")

# s1 = B("kumar","c",102)
# s1.display()  

# class C(A,B):
#     # def __init__(self,name,salary,subject,Roll_no):
#     #     A.__init__(self,name,salary)
#     #     B.__init__(self,name,subject,Roll_no)   
    
  # =============  pass ka bi use kar skate hai =================  
#     pass

#=================multilevel inhretance ========================

# class parent1:
#     def color(self):
#         print("red")
# class parent2(parent1):
#     def height(self):
#         print("6 feet")  
# class child(parent2):
#     def weight(self):
#         print("70 kg")
# c1 = child()
# c1.color() 
# c1.height()
# c1.weight()



#2nd type of multilevel inheritance

# class parent1:
#     def __init__(self,hair_color,eyes_color):
#         self.hair_color = hair_color
#         self.eyes_color = eyes_color
#     def display(self):
#         print(f"hair color is {self.hair_color}")
#         print(f"eyes color is {self.eyes_color}")
# class parent2(parent1):
#     def __init__(self,hair_color,eyes_color,height):
#         super().__init__(hair_color,eyes_color)
#         self.height = height
#     def display(self):
#         super().display()
#         print(f"height is {self.height}")
# class child(parent2):
#     def __init__(self,hair_color,eyes_color,height,weight):
#         super().__init__(hair_color,eyes_color,height)
#         self.weight = weight
#     def display(self):
#         super().display()
#         print(f"weight is {self.weight}")
# c1 = child("black","brown","6 feet","70 kg")
# c1.display()


#===============3rd type of multilevel inheritance========================

class A:
    def __init__(self,hair_color):
        self.hair_color = hair_color
class B(A):
    def __init__(self,hair_color,eyes_color):
        super().__init__(hair_color)
        self.eyes_color = eyes_color
class C(B):
    pass

c1 = C("black","brown")
print(f"Hair color is {c1.hair_color}")
print(f"Eyes color is {c1.eyes_color}")