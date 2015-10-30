# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.PositiveIntegerField(help_text=b'Following user UID', db_index=True)),
                ('follower_uid', models.PositiveIntegerField(db_index=True)),
                ('follow_time', models.DateTimeField(help_text=b'time of start following', db_index=True)),
            ],
            options={
                'db_table': 'follower',
            },
        ),
        migrations.CreateModel(
            name='Microblog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.PositiveIntegerField(db_index=True)),
                ('blog', models.CharField(max_length=2048)),
                ('post_time', models.DateTimeField(db_index=True)),
                ('poster', models.PositiveIntegerField(help_text=b'Poster of the blog', db_index=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='microblog.Microblog', null=True)),
            ],
            options={
                'db_table': 'microblog',
            },
        ),
    ]
