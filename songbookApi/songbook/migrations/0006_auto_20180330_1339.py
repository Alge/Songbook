# Generated by Django 2.0.3 on 2018-03-30 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0005_auto_20180330_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verse',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verses', to='songbook.Song'),
        ),
    ]
