# Generated by Django 2.2.3 on 2020-02-02 14:01

from django.db import migrations, models
import django_matplotlib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bip', '0005_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelWithFigure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fig', django_matplotlib.fields.MatplotlibFigureField()),
            ],
        ),
    ]