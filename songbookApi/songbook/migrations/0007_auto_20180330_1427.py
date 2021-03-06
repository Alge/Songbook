# Generated by Django 2.0.3 on 2018-03-30 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0006_auto_20180330_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Melody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='melody',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songbook.Melody'),
        ),
    ]
