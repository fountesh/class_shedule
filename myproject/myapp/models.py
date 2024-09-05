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