# Generated by Django 3.2.3 on 2021-05-28 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('idade', models.IntegerField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
