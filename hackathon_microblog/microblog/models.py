from django.db import models

class Follower(models.Model):
    uid = models.PositiveIntegerField(help_text='Following user UID', db_index=True)
    follower_uid = models.PositiveIntegerField(db_index=True)
    follow_time = models.DateTimeField(help_text='time of start following', db_index=True)

    class Meta:
        db_table = 'follower'

class Microblog(models.Model):
    uid = models.PositiveIntegerField(db_index=True)
    blog = models.CharField(max_length=2048)
    post_time = models.DateTimeField(db_index=True)
    poster = models.PositiveIntegerField(help_text='Poster of the blog', db_index=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'microblog'
