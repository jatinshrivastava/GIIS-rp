# Generated by Django 2.2.2 on 2019-10-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_status',
            field=models.CharField(default='parent', max_length=20),
        ),
    ]
