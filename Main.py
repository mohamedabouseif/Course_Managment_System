
from Teacher import Teaher
import linecache
from student import *


Teaher()
student()
#print(t1)
print('______________________________________________:')
print('Hello to our course system !')
print('____________________________________________ :')
print()

i = 1
switch =False

while True:
    try:
        choice = int(input(' ==> to login as teacher press 1 ,as student press 2 and 3 to exit  : \n'))

        if choice == 1:
            teach= Teaher()
            teach.Log_in()

        elif choice == 2:
            stu = student()
            stu.get_into()
        elif choice ==3:
            print('(^_^) GoodLuck !')
            break
        else:
            print('(^_^) Wrong choice , try again !')

    except Exception as e :
        print(e)
        print('Please Enter Integer numbers only !')
        line = linecache.getline('Main.py',20)