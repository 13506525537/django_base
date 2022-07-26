# Generated by Django 4.0.6 on 2022-07-23 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('pub_date', models.DateField(null=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female')])),
                ('book', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo')),
            ],
            options={
                'db_table': 'peopleinfo',
            },
        ),
    ]
