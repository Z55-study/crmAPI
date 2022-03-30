from django.db import models

STATUS_CHIEF = [
    ('0', 'Сам себе начальник'),
    ('1', 'Генеральный директор'),
    ('2', 'Директор(a)'),
    ('3', 'Зам Директор(а)'),
    ('4', 'Начальник(a) Отдела'),
]

STATUS_PERSON = [
    ('0', 'Генеральный директор'),
    ('1', 'Директор'),
    ('2', 'Зам Директора'),
    ('3', 'Начальник Отдела'),
    ('4', 'Рабочий')
]


class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО', null=True)
    position = models.CharField(max_length=255, choices=STATUS_PERSON, verbose_name='Должность', null=True)
    employment_date = models.DateField(null=True, verbose_name='Дата приема на работу', blank=True)
    salary = models.CharField(max_length=255, verbose_name='Размер ЗП')
    information_salary = models.CharField(max_length=255, verbose_name='Инф о выплаченной ЗП', null=True)
    chief = models.CharField(max_length=10, choices=STATUS_CHIEF, verbose_name='В подчинении у ')

    class Meta:
        verbose_name = 'Сотрудник(а)'
        verbose_name_plural = 'Сотрудники(а)'
