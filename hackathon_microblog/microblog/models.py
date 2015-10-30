from django.db import models

class Follower(models.Model):
    uid = models.PositiveIntegerField(help_text='Following user UID', db_index=True)
    follower_uid = models.PositiveIntegerField(db_index=True)
    follow_time = models.DateTimeField(help_text='time of start following', db_index=True)

    class Meta:
        db_table = 'follower'


class BaseBlog(models.Model):
    uid = models.PositiveIntegerField(help_text='Poster of the blog', db_index=True)
    post_time = models.DateTimeField(db_index=True)
    blog = models.CharField(max_length=2048)
    
    class Meta:
        abstract = True

class Microblog(BaseBlog):
    class Meta:
        db_table = 'microblog'

class Comment(BaseBlog):
    comment_blog = models.ForeignKey(Microblog, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'blog_comment'
