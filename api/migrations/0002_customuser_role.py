# Generated by Django 4.0 on 2022-08-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Restaurant', 'Restaurant')], max_length=10, null=True),
        ),
    ]
