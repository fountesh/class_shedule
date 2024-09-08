from django.db import models

# Create your models here.

class Subject(models.Model):
    s_name = models.CharField(max_length=100)

    def __str__(self):
        return self.s_name

class Teacher(models.Model):
    l_name = models.CharField(max_length=100)
    s_name = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.l_name

class Class(models.Model):
    c_num = models.IntegerField()

    def __str__(self):
        return self.c_num

class Student(models.Model):
    f_name = models.CharField(max_length=100)
    c_num = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name

class Shedule(models.Model):
    day = models.CharField(max_length=100, choices=[("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Thursday", "Thursday"), ("Friday", "Friday")])
    begining = models.TimeField()
    s_name = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    c_num = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    l_name = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.day}: {self.begining}"

class Grade(models.Model):
    f_name = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    s_name = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.f_name}: grade is {self.grade},"
