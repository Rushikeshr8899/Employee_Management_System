# Generated by Django 4.2 on 2023-04-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10),
        ),
    ]