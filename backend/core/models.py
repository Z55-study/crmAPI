from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    # level = models.CharField(max_length=255)
    employment_date = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    information_salary = models.CharField(max_length=255)
    department_one = models.CharField(max_length=255)
    department_tw = models.CharField(max_length=255)
    department_thr = models.CharField(max_length=255)
    department_fo = models.CharField(max_length=255)



