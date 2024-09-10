import sys
import os
import django



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import Subject, Teacher, Class, Student, Shedule, Grade

# sub1 = Subject(
#         s_name = "maths"
#     )

# teach1 = Teacher(
#         l_name = "Lenina",
#         s_name = sub1
#     )

# class1 = Class(
#         c_num = 10
#     )

# stud1 = Student(
#         f_name = "Ivan",
#         c_num = class1
#     )

# sub1.save()
# teach1.save()
# class1.save()
# stud1.save()
# stud2 = Student.objects.get(id = 2)
# stud2.f_name = "Anton"
# stud2.save()

while True:
    user = input("0-вийти, 1-додавання предмету, 2-додавання вчителя, 3-додавання класу, 4-додавання учня, 5-додавання розкладу, 6-додавання оцінки: ")
    if user == "0":
        break
    
    elif user == "1":
        sub_name = input("Назву предмета: ")
        new_sub = Subject.objects.create(s_name = sub_name)
        print("Успішно створено!")
    
    elif user == "2":
        teach_name = input("Прізвище вчителя: ")
        sub_name = input("Назва предмета: ")
        sub_list = Subject.objects.get(s_name = sub_name)
        if sub_list:
            new_teach = Teacher.objects.create(l_name = teach_name, s_name = sub_list)
            print("Успішно створено!")
    
    elif user == "3":
        clas_num = int(input("Введи клас: "))
        new_clas = Class.objects.create(c_num = clas_num)
        print("Успішно створено!")
    
    elif user == "4":
        stud_name = input("ім'я учня: ")
        clas_num = int(input("Введи клас: "))
        clas_list = Class.objects.get(c_num = clas_num)
        if clas_list:
            new_stud = Student.objects.create(f_name = stud_name, c_num = clas_list)
            print("Успішно створено!")
    
    elif user == "5":
        n_day = input("Введи день тижня: ")
        n_begining = input("Введи час: ")
        sub_name = input("Назву предмета: ")
        clas_num = int(input("Введи клас: "))
        teach_name = input("Прізвище вчителя: ")
        
        sub_list = Subject.objects.get(s_name = sub_name)
        clas_list = Class.objects.get(c_num = clas_num)
        teach_list = Teacher.objects.get(l_name = teach_name)
        if sub_list and clas_list and teach_list:
            new_shed = Shedule.objects.create(day=n_day, begining = n_begining, s_name=sub_list, c_num = clas_list, l_name = teach_list)
            print("Успішно створено!")
    
    elif user == "6":
        stud_name = input("ім'я учня: ")
        sub_name = input("Назву предмета: ")
        n_grade = int(input("Введи оцінку: "))
        f_name_list = Student.objects.get(f_name = stud_name)
        sub_list = Subject.objects.get(s_name = sub_name)
        if f_name_list and sub_list:
            new_grade = Grade.objects.create(f_name = f_name_list, s_name = sub_list, grade = n_grade)
            print("Успішно створено!")
        