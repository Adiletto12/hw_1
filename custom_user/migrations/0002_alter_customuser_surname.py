# Generated by Django 5.0.3 on 2024-04-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='surname',
            field=models.TextField(max_length=40, null=True),
        ),
    ]
