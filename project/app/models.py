from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.IntegerField(verbose_name='Дом')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural ='Адреса'
        ordering = ('city',)

    def get_full_address(self):
        return f'{self.city}, {self.street}, {self.house}'


class University(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    address = models.OneToOneField(Address,  on_delete=models.CASCADE, verbose_name='Адрес', related_name='university')

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural ='Университеты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
        ordering = ('name', )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Кафедра', related_name='teacher')
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    surname2 = models.CharField(max_length=255, verbose_name='Отчество')
    birth = models.IntegerField(verbose_name='Год рождения')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural ='Преподаватели'
        ordering = ('department', 'name', 'surname')

    def __str__(self):
        return self.name

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.surname2}'
