# Generated by Django 4.1.4 on 2022-12-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, unique=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('category', models.CharField(choices=[('C1', 1), ('C2', 2), ('C3', 3)], max_length=3)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]