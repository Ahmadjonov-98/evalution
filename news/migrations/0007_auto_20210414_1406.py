# Generated by Django 3.2 on 2021-04-14 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_article_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employee',
        ),
    ]
