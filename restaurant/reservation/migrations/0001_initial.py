# Generated by Django 5.2 on 2025-04-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=50, verbose_name='پست الکترونیکی')),
                ('phone', models.IntegerField(max_length=13, verbose_name='شماره همراه')),
                ('number', models.IntegerField(max_length=50, verbose_name='تعداد')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('time', models.TimeField(verbose_name='ساعت')),
            ],
        ),
    ]
