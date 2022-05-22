# Generated by Django 4.0.4 on 2022-05-20 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarHub', '0002_model')
    ]

    operations = [
        migrations.CreateModel(
            name='Oglas',
            fields=[
                ('idoglas', models.AutoField(db_column='idOglas', primary_key=True, serialize=False)),
                ('tip', models.CharField(db_column='Tip', max_length=1)),
                ('cena', models.IntegerField(blank=True, db_column='Cena', null=True)),
                ('boost', models.IntegerField(blank=True, db_column='Boost', null=True)),
                ('grad', models.CharField(db_column='Grad', max_length=45)),
                ('slike', models.FileField(db_column='Slike', null=True, upload_to='imgs/')),
                ('model_idmodel', models.ForeignKey(db_column='Model_idModel', on_delete=django.db.models.deletion.DO_NOTHING, to='CarHub.model')),
            ],
        ),
    ]