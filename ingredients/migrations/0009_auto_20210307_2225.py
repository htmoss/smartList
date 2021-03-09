# Generated by Django 3.1.7 on 2021-03-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0008_auto_20210307_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric', models.CharField(default='', max_length=20, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]