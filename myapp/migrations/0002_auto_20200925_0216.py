# Generated by Django 2.2.3 on 2020-09-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='keyword',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
