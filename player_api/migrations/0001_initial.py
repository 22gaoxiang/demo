# Generated by Django 3.0.4 on 2020-03-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(default='', help_text='客户端', max_length=50, verbose_name='客户端')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
