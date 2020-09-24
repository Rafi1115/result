# Generated by Django 3.1.1 on 2020-09-24 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0012_auto_20200923_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.class_alim')),
                ('dakhil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.class_dakhil')),
            ],
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='semes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.semester'),
        ),
    ]