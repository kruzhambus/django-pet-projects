# Generated by Django 3.2.7 on 2021-10-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='specifications',
            field=models.FileField(upload_to='photos/%Y/%m/%d/', verbose_name='Документ'),
        ),
    ]
