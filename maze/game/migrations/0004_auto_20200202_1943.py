# Generated by Django 3.0.1 on 2020-02-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20200111_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='moves',
            new_name='lose',
        ),
        migrations.AddField(
            model_name='profile',
            name='win',
            field=models.IntegerField(default=0),
        ),
    ]
