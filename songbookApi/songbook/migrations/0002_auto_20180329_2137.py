# Generated by Django 2.0.3 on 2018-03-29 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
