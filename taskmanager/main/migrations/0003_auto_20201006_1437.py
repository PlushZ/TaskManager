# Generated by Django 3.1.2 on 2020-10-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201005_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
    ]
