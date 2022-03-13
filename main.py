#Malik Muhammad Kashif Saeed(Solution Master);
import math
class Maths_method:

    def square_root(n):
        sqrt=n*n;
        return sqrt;
    def factorial(num):
        fac=1;
        while(num !=0):
            fac=fac*num;
            num-=1;
        return fac;
    def Log(num):
        i=True;
        while(i !=False):
            print("What type of log you want to take? ");
            print("1. Natural Log\n2. Log with base e");
            option = int(input("Enter Option: "));
            if (option == 1):
                return math.log(num)
            elif (option == 2):
                base = input("Enter Base: ");
                return math.log(num, base);
            else:
                i = True;
                print("Invalid option.");


print("Welcome to the simple math helper");
opt=True;
while(opt != False):


    print("IF YOU WANT TO EXIT ENTER y/n");
    op = input("Enter y/n: ");

    if(op == 'y'):
        opt=False;
    elif(op == 'n'):
        print("What would you like to do?");
        print("1.Sqrt\n2.Factorial\n3.Log");
        option = int(input("Enter the option: "));
        num = int(input("Enter the Number for Evaluation: "));

        if(option == 1):

            print("Sqaure Root of ",num," is: ",Maths_method.square_root(num));
        elif(option == 2):
            facObj=Maths_method();
            print("Factorial of a " ,num , " is: ", Maths_method.factorial(num));
        elif(option == 3):
            print("Log Of a Number: ",Maths_method.Log(num));
        else:
            print("Invalid Number.")


        print("Welcome to the simple math helper Again.:) ");





#print("What would you like to do?");
#print("1.Sqrt\n2.Log\n3.Factorial");
#print(Maths_method.square_root(5));
#print(Maths_method.factorial(5));
