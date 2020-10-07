# Generated by Django 3.1.2 on 2020-10-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201006_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('N', 'Новая'), ('P', 'Запланированная'), ('S', 'В работе'), ('C', 'Завершенная')], default='N', max_length=2, verbose_name='Статус'),
        ),
    ]