from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок объявления')
    id_announcement = models.IntegerField(unique=True, verbose_name='id объявления')
    author = models.CharField(max_length=100, verbose_name='Автор объявления')
    count_views = models.IntegerField(verbose_name='Количество просмотров объявления')
    position = models.IntegerField(verbose_name='Позиция объявления')

    class Meta:
        db_table = 'announvements'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
