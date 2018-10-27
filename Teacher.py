import getpass
import linecache

class Teaher:


    student_info = {'Justin':93,'Mario':75}

    Teacher_name = 'm'
    Teacher_password = '123'
    print('I\'m the Teachere class')



    def Log_in(self):     # complete and work


        while True:
            attrmpts =0
            if  attrmpts <= 3:
                user = str(input('Enter user name : '))
                password = getpass.getpass("Enter Your Password Here: ")


                if user == self.Teacher_name and password ==self.Teacher_password:
                    print('Hey , {}'.format(self.Teacher_name))
                    self.operations()
                    break
                else:
                    print('Incorrect , try again !')
                attrmpts +=1

            else:
                print('Alarm , Hacker detection !')
                break

    def operations(self):
        try:# complete and work

            while True:
                select = int(input('press 1 to Add new student ,2 to Edit grade ,3 to Delete student ,'
                                   '4 to Search , 5 to  show all ,6 to exit:\n '))
                if select == 1:
                    self.AddStudent()
                    break
                elif select == 2:
                    self.grades()
                    break
                elif select == 3:
                    self.Delete()
                elif select == 4:
                    self.searchFor()
                    break
                elif select == 5:
                    self.Show_all()
                    break

                elif select ==6 :
                    print('^_^ GoodLuck !')
                    break
                else:
                    print('incorrect selection ,try again  !')
        except Exception as e:
            print(e)
            print('Please Enter only Integer numbers !')
            self.operations()
    def grades(self): #complete and work
        try:
            while True:
                UserName=input('Enter student username : ')
                grade =int(input('Enter grade : '))
                for k, v in self.student_info.items():
                    if k == UserName:
                        print('key = ', k)
                        print('Value = ', v)
                        self.student_info[k] = grade
                        print(self.student_info)
                        self.operations()

                else:
                    print('There is\'n student with this username! ')
                    select= int(input('to try again press 1 to exit press 2 :\n'))
                    if select ==1 :
                        self.grades()
                    elif select == 2:
                        print('Exit now !')
                        break
                    else:
                        print('Error , try again !')
        except Exception as e:
            print(e)

    def searchFor(self):  # complete and work
        try:
            while True:
                UserName=input('Enter student username : ')
                for k, v in self.student_info.items():
                    if k == UserName:
                        print('+----------------------+')
                        print(' Student Name :', k)
                        print('grade is : ',v)
                        print('+----------------------+')

                        self.operations()

                else:
                    print('There is\'n student with this username! ')
                    select= int(input('to try again press 1 to exit press 2 :\n'))
                    if select ==1 :
                        self.searchFor()
                    elif select == 2:
                        print('Exit now !')
                        self.operations()
                    else:
                        print('Error , try again !')
        except Exception as e:
            print(e)

    def AddStudent(self):
        try:
            while True:
                _user = (str(input('Enter student userName : ')))
                _password = (int(input('Enter grade :')))
                for k, v  in self.student_info.items():
                    if k==_user:
                        print('Key :' ,k)
                        print('values :',v)
                        print('This Student Already Exit !')
                        break
                else:
                    self.student_info[_user]=_password
                    print('Student Added !')
                    print(self.student_info)
                    select=int(input('Continue press 1 ,2 to exit :'))
                    if select == 1:
                        self.AddStudent()

                    elif select == 2:
                        self.operations()

                    else:
                        print('Wrong input , try again')
                        self.operations()
        except Exception as e :
            print(e)
            self.operations()

    def Delete(self):
        try:

            while True:
                user=str(input('Enter Student Username : '))
                for k , v  in self.student_info.items():
                    if k ==user :
                        del self.student_info[k]
                        print(k,' has been deleted !')
                        self.operations()
                else:
                    print('No student exit with this Username')
                    print('Try again !')
                    self.Delete()


        except Exception as e :
            print(e)
            self.Delete()

    def Show_all(self):  # compltete and work
        for k, v in self.student_info.items():
            print('+------------------------------------------------+')
            print('studentName : ',k ,'--> ','grade is : ' ,v)
            print('+------------------------------------------------+')
        self.operations()

