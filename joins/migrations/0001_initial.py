# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('ref_id', models.CharField(unique=True, max_length=120, default='ABC')),
                ('ip_address', models.CharField(max_length=120, default='ABC')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('friend', models.ForeignKey(related_name='referral', to='joins.Join', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]
