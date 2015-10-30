# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.PositiveIntegerField(help_text=b'Poster of the blog', db_index=True)),
                ('post_time', models.DateTimeField(db_index=True)),
                ('blog', models.CharField(max_length=2048)),
            ],
            options={
                'db_table': 'blog_comment',
            },
        ),
        migrations.RemoveField(
            model_name='microblog',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='microblog',
            name='poster',
        ),
        migrations.AlterField(
            model_name='microblog',
            name='uid',
            field=models.PositiveIntegerField(help_text=b'Poster of the blog', db_index=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='microblog.Microblog', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='microblog.Comment', null=True),
        ),
    ]
