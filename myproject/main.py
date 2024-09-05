import sys
import os
import django



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import Subject, Teacher, Class, Student

sub1 = Subject(
        s_name = "maths"
    )

teach1 = Teacher(
        l_name = "Lenina",
        s_name = sub1
    )

class1 = Class(
        c_num = 10
    )

stud1 = Student(
        f_name = "Ivan",
        c_num = class1
    )

sub1.save()
teach1.save()
class1.save()
stud1.save()
