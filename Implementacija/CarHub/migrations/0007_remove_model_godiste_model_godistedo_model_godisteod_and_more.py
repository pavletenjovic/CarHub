# Generated by Django 4.0.4 on 2022-05-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

        ('CarHub', '0006_remove_model_karoserija_remove_model_kilometraza_and_more')

    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='godiste',
        ),
        migrations.AddField(
            model_name='model',
            name='godisteDo',
            field=models.IntegerField(db_column='GodisteDo', default=0),
        ),
        migrations.AddField(
            model_name='model',
            name='godisteOd',
            field=models.IntegerField(db_column='GodisteOd', default=0),
        ),
        migrations.AddField(
            model_name='oglas',
            name='godiste',
            field=models.IntegerField(db_column='Godiste', default=0),
        ),
    ]