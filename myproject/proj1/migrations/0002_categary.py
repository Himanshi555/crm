# Generated by Django 2.1.4 on 2019-01-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=128)),
            ],
        ),
    ]