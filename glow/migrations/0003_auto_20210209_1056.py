# Generated by Django 3.1.6 on 2021-02-09 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glow', '0002_auto_20210209_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='routine',
        ),
        migrations.AddField(
            model_name='routine',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='glow.comment'),
            preserve_default=False,
        ),
    ]
