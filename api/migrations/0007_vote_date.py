# Generated by Django 4.0 on 2022-08-17 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_menu_votes_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
