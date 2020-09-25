# Generated by Django 3.1.1 on 2020-09-25 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('year', models.IntegerField(choices=[(2020, 2020), (2019, 2019), (2018, 2018)])),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.board')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('point', models.FloatField()),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
                'db_table': '',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.board')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects_of_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sub1', models.CharField(max_length=50)),
                ('sub2', models.CharField(max_length=50)),
                ('sub3', models.CharField(max_length=50)),
                ('sub4', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('mother_name', models.CharField(max_length=45)),
                ('father_name', models.CharField(max_length=45)),
                ('date_of_birth', models.DateField()),
                ('roll', models.IntegerField()),
                ('group', models.CharField(choices=[('A', 'Arts'), ('C', 'Commerce'), ('S', 'Science')], max_length=1)),
                ('result', models.CharField(blank=True, choices=[('F', 'FAILED'), ('P', 'PASSED')], max_length=1)),
                ('gpa', models.FloatField(blank=True, null=True)),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.board')),
                ('dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.course')),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.exam')),
                ('institute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='results.school')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='student',
            field=models.ManyToManyField(to='results.StudentInfo'),
        ),
        migrations.AddField(
            model_name='school',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='subjects_of_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.subjects_of_class'),
        ),
    ]
