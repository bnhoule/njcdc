# Generated by Django 2.0.3 on 2018-04-20 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20180420_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gasoline_type',
            field=models.CharField(choices=[('e10', 'Regular Gasoline'), ('e0', 'Pure Gasoline'), ('diesel', 'Diesel'), ('b20', '20% Biodiesel')], default='e10', max_length=40),
        ),
    ]