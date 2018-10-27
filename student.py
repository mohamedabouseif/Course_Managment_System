from Teacher import *
class student(Teaher):
    print('I\'m the student class')
    try:
        def get_into(self):
            s_user= str(input('Enter your username : '))
            for k, v in self.student_info.items():
                if k == s_user:
                    print('+----------------------+')
                    print(' Student Name :', k)
                    print('grade is : ', v)
                    print('+----------------------+')
                    break

            else:
                print('Error , Try again')
                self.get_into()


    except Exception as e :
        print(e)