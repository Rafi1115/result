# Generated by Django 3.1.1 on 2020-09-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20200922_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='year',
            field=models.IntegerField(choices=[('200', '2020'), ('2019', '2019'), ('1992', '1992')]),
        ),
    ]