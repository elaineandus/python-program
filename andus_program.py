# Program Description: Write a Python program that displays a menu to the user with different options to choose from. Depending on the user's input, the program will execute a certain function.

import math
def switch():
    print("\033[1m******************************\033[0m")
    print("\033[1m|\033[0m   \033[1mSelect an option:\033[0m        \033[1m|\033[0m")
    print("\033[1m******************************\033[0m")
    print("\033[1m|\033[0m   \033[1m1. Array            \033[0m     \033[1m|\033[0m")
    print("\033[1m|\033[0m   \033[1m2. Nested Loop      \033[0m     \033[1m|\033[0m")
    print("\033[1m|\033[0m   \033[1m3. Sequential Program\033[0m    \033[1m|\033[0m")
    print("\033[1m|\033[0m   \033[1m4. Conditional Program\033[0m   \033[1m|\033[0m")
    print("\033[1m|\033[0m   \033[1m5. Loops Program    \033[0m     \033[1m|\033[0m")
    print("\033[1m|\033[0m   \033[1m6. Credits          \033[0m     \033[1m|\033[0m")
    print("\033[1m|\033[0m   \033[1m7. Exit             \033[0m     \033[1m|\033[0m")
    print("\033[1m******************************\033[0m")
 
    option = int(input("Enter the number of your choice: "))
    print()

    def Array():
        lst = []
        num = int(input("Enter a size of an array from 1-10: "))
        print()
        print("Input {0} numbers: ".format(num))
        for n in range(num):
         numbers = int(input())
         lst.append(numbers)
        print()
        print("The even numbers are: ")
        for numbers in lst:
            if numbers % 2 == 0:
                
                print(numbers, end=" ")
        print("\nThe Sum of all the numbers is: ", sum(lst))
        
        print()
        back = (input("Back to Menu? Press Y-yes/N-no: "))
        if back == 'Y' or back == 'y':
            switch()
        elif back == 'N' or back == 'n':
            quit()
        else:
            print("Please choose Y or N only.")
        

    def NestedLoop():
     rows = int(input("Enter a number to display: "))
     for i in range(rows, 0, -1):
            num = i

            for j in range(0, i):
      
              
                  print(num, end='')
            print("\r")
     print()
     back = (input("Back to Menu? Press Y-yes/N-no: "))
     if back == 'Y' or back == 'y':
          switch()
     elif back == 'N' or back == 'n':
         quit()
     else:
         print("Please choose Y or N only.")
          
            
        

    def Sequentialprogram():
        print("Compute for the Circumference of a Circle:")
        num = int(input("Enter a radius: "))
        result = 2*math.pi*num
        circumference = float(result)
        floatcircumference = '{0:.2f}'.format(circumference)
        print("The circumference of a circle is: ", floatcircumference)

        print()
        back = (input("Back to Menu? Press Y-yes/N-no: "))
        if back == 'Y' or back == 'y':
                switch()
        elif back == 'N' or back == 'n':
                quit()
        else:
                print("Please choose Y or N only.")
        
    
    def Conditionalprogram():
            print("Enter 3 numbers:")
            loopcount = 0
            highest = -float('inf')  
           
            while loopcount < 3:
              loopcount = loopcount + 1

              given = input()
              given_as_integer = int(given)
        
              if given_as_integer > highest:
                highest = given_as_integer

            print('The highest number is: ', highest)
            print()
            back = (input("Back to Menu? Press Y-yes/N-no: "))
            if back == 'Y' or back == 'y':
                switch()
            elif back == 'N' or back == 'n':
                quit()
            else:
                print("Please choose Y or N only.")
        
    def Loopsprogram():
        
        n1 = int(input("Enter a number for loops: "))
        print()
        for x in range(n1, 0, -1):
            num = x
            print(num, end=' ')
        
        print()
        back = (input("\nBack to Menu? Press Y-yes/N-no: "))
        if back == 'Y' or back == 'y':
                switch()
        elif back == 'N' or back == 'n':
                quit()
        else:
                print("Please choose Y or N only.")
    def Credits():

        print("Thanks for using my Program!!!")
        print()
        print("Programmer Name: Andus, Elaine S.")
        print()
        back = (input("Back to Menu? Press Y-yes/N-no: "))
        if back == 'Y' or back == 'y':
                switch()
        elif back == 'N' or back == 'n':
                quit()
        else:
                print("Please choose Y or N only.") 
                
    def Exit():
        
        quit()

    def default():
        print("Choose only from 1-7.")
 

    dict = {

       
        1 : Array,
        2 : NestedLoop,
        3 : Sequentialprogram,
        4 : Conditionalprogram,
        5 : Loopsprogram,
        6 : Credits,
        7 : Exit,       
 
    }
    
    dict.get(option,default)() 
 

switch()

