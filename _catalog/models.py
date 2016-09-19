from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Страна', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Region(models.Model):
    country = models.ForeignKey(Country,blank=False)
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Регион', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class City(models.Model):
    country = models.ForeignKey(Country, blank=False, null=False, verbose_name='Страна')
    region = models.ForeignKey(Region, blank=False, null=False, verbose_name='Регион')
    name = models.CharField(max_length=128,null=False, blank=False, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
