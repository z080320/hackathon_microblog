from rest_framework import serializers
from hackathon_microblog.microblog.models import Microblog, Comment, Follower
import datetime
import pytz

class BaseBlogSerializer(serializers.ModelSerializer):
    blog_post_time = serializers.SerializerMethodField()

    def get_blog_post_time(self, obj):
        sgt = pytz.timezone('Singapore')
        post_time_sgt = obj.post_time.astimezone(sgt)
        timestr = post_time_sgt.strftime('%Y-%m-%d %H:%M:%S %p')
        return timestr

class MicroblogSerializer(BaseBlogSerializer):
    class Meta:
        model = Microblog
        fields = ('id', 'uid', 'blog', 'blog_post_time')

class CommentSerializer(BaseBlogSerializer):
    parent_id = serializers.SerializerMethodField()
    parent_uid = serializers.SerializerMethodField()

    def get_parent_id(self, obj):
        parent = obj.parent
        if parent:
            parent_id = parent.id
        else:
            parent_id = 0
        return parent_id

    def get_parent_uid(self, obj):
        parent = obj.parent
        if parent:
            parent_uid = parent.uid
        else:
            parent_uid = None

        return parent_uid

    class Meta:
        model = Comment
        fields = ['id', 'uid', 'blog', 'blog_post_time', 'comment_blog', 'parent_id', 'parent_uid']


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'uid', 'follower_uid', 'follow_time', ]

