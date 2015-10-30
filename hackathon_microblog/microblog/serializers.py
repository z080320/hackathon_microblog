from rest_framework import serializers
from hackathon_microblog.microblog.models import Microblog, Comment, Follower

class MicroblogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microblog
        fields = ('id', 'uid', 'blog', 'post_time')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'uid', 'blog', 'post_time', 'comment_blog', 'parent']


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'uid', 'follower_uid', 'follow_time', ]

