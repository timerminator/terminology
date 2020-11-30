from django.db import models


# Справочник
class Handbook(models.Model):
    title = models.CharField(max_length=120, verbose_name='Наименование')
    short_title = models.CharField(max_length=30, verbose_name='Короткое наименование')
    description = models.TextField(verbose_name='Описание')
    version = models.CharField(max_length=50, verbose_name='Версия')
    start_date = models.DateField(verbose_name='Дата начала')

    def __str__(self):
        return f'{self.title} версия: {self.version}'

    class Meta:
        unique_together = ('title', 'version')


# Элементы справочника
class ElementHandbook(models.Model):
    handbook_id = models.ForeignKey(Handbook, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, verbose_name='Код элемента')
    value = models.CharField(max_length=200, verbose_name='Значение элемента')

    def __str__(self):
        return f'Элемент {self.code}'

