# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20150807_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('catalogue_number', models.CharField(max_length=38)),
                ('cover_type', models.CharField(choices=[('soft', 'Soft'), ('hard', 'Hard')], max_length=4)),
                ('edition', models.ForeignKey(to='shelf.BookEdition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bookitems',
            name='edition',
        ),
        migrations.DeleteModel(
            name='BookItems',
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(verbose_name='first name', max_length=20),
            preserve_default=True,
        ),
    ]
