from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=150, blank=False)
    task = models.TextField('Описание', max_length=300, blank=False)
    date = models.DateTimeField('Время создания', auto_now_add=True)
    STATUSES = (
        ('N', 'Новая'),
        ('P', 'Запланированная'),
        ('S', 'В работе'),
        ('C', 'Завершенная'),
    )
    status = models.CharField('Статус', max_length=2, choices=STATUSES, default=STATUSES[0][0], blank=False)
    date_end = models.DateField('Дата завершения', null=True, blank=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'