'''
Objective 
In this challenge, we're going to learn about the difference between a class and an instance;
 because this is an Object Oriented concept, it's only enabled in certain languages. 
 Check out the Tutorial tab for learning materials and an instructional video!

Task 
Write a Person class with an instance variable, age , and a constructor that takes an integer, initialAge , as a parameter. 
The constructor must assign initialAge to age  after confirming the argument passed as initialAge  is not negative; 
if a negative argument is passed as initialAge, the constructor should set age to 0 and print Age is not valid, 
setting age to 0.. In addition, you must write the following instance methods:

yearPasses() should increase the age instance variable by 1.
amIOld() should perform the following conditional actions:
1) If  age=<13 , print You are young..
2)If age>=13 and age < 18 , print You are a teenager..
3)Otherwise, print You are old..
To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.

Input Format

Input is handled for you by the stub code in the editor.

The first line contains an integer,  (the number of test cases), and the  subsequent lines each contain an integer denoting the  of a Person instance.

Constraints

Output Format

Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print  or lines (depending on whether or not a valid  was passed to the constructor).

Sample Input

4
-1
10
16
18
Sample Output

Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
'''
'''
class Person:
    age = 0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        # age = 0
        if initialAge<0:
            self.initialAge=age
            print('Age is not valid, setting age to 0.')
        else:
            self.age=initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age<13:
            print('You are young.')
        elif age >=13 and age <18:
            print('You are teenager')
        elif age >=18:
            print('You are old')

    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age += 1
        return age
'''

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = 0
        self.initialAge = initialAge
        if initialAge < 0:
            print ('Age is not valid, setting age to 0.')
        else:
            initialAge = self.age


    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge < 13:
            print ('You are young.')
        elif 13 <= self.initialAge < 18:
            print ('You are a teenager.')
        else:
            print ('You are old.')


    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge += 1
t=int(input())
for i in range(0,t):
    age=int(input())
    p=Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")