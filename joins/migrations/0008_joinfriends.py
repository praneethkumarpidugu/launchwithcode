# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0007_auto_20150310_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinFriends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.OneToOneField(to='joins.Join', related_name='Sharer')),
                ('emailall', models.ForeignKey(to='joins.Join', related_name='emailall')),
                ('friends', models.ManyToManyField(to='joins.Join', blank=True, related_name='Friend', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
