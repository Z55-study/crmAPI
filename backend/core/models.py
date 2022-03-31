from django.db import models


class Person(models.Model):
    STATUS_CHIEF = [
        ('0', 'Генеральный директор'),
        ('1', 'Директор(a)'),
        ('2', 'Зам Директор(а)'),
        ('3', 'Начальник(a) Отдела'),
    ]

    STATUS_PERSON = [
        ('0', 'Генеральный директор'),
        ('1', 'Директор'),
        ('2', 'Зам Директора'),
        ('3', 'Начальник Отдела'),
        ('4', 'Рабочий')
    ]

    full_name = models.CharField(max_length=15, verbose_name='ФИО', null=True)
    position = models.CharField(max_length=1, choices=STATUS_PERSON, verbose_name='Должность')
    employment_date = models.DateField(verbose_name='Дата приема на работу', null=True, blank=True)
    salary = models.PositiveSmallIntegerField(verbose_name='Размер ЗП')
    information_salary = models.PositiveIntegerField(verbose_name='Инф о выплаченной ЗП', null=True, blank=True)
    chief = models.CharField(max_length=1, choices=STATUS_CHIEF, verbose_name='В подчинении у ', null=True, blank=True)

    class Meta:
        verbose_name = 'Сотрудник(а)'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name
