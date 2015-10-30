from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from gtoext.rest import SuccessResponse
from gtoext.contrib.garena_oauth.user import AuthGarenaUser, PermitGarenaUser302, PermitGarenaUser
from hackathon_microblog.microblog import helper
from hackathon_microblog.microblog import serializers

import pprint

import logging
LOG = logging.getLogger("main")


class ProtectedTemplateView(APIView):
    template_name = ''

    renderer_classes = (TemplateHTMLRenderer, )
    authentication_classes = (AuthGarenaUser, )
    permission_classes = (PermitGarenaUser302, )

    def get(self, request, *args, **kwargs):
        kwargs.update({'user': request.user,
                       'nickname': request.user.nickname, })
        return SuccessResponse(kwargs, template_name=self.__class__.template_name)

class ProtectedBaseAPIView(APIView):
    authentication_classes = (AuthGarenaUser,)
    permission_classes = (PermitGarenaUser, )


class HomeBlogAPIView(ProtectedBaseAPIView):
    def get(self, request, *args, **kwargs):
        uid = request.user.uid
        recent_blogs = helper.get_followee_recent_blog(uid)
        pprint.pprint(recent_blogs)

        blog_serializer = serializers.MicroblogSerializer(recent_blogs, many=True)
        return SuccessResponse(blog_serializer.data)

    def post(self, request, *args, **kwargs):
        uid = request.user.uid
        blog = request.POST.get('blog')

        helper.post_microblog(uid, blog)
        return SuccessResponse({'success': True})


class MicroblogAPIView(ProtectedBaseAPIView):
    def get(self, request, *args, **kwargs):
        uid = request.user.uid
        recent_blogs = helper.get_user_recent_blog(uid)

        blog_serializer = serializers.MicroblogSerializer(recent_blogs, many=True)
        return SuccessResponse(blog_serializer.data)


class CommentAPIView(ProtectedBaseAPIView):
    def get(self, request, blog_id):
        uid = request.user.uid
        blog_comments = helper.get_blog_comments(uid, blog_id)

        comments_serializer = serializers.CommentSerializer(blog_comments, many=True)
        return SuccessResponse(comments_serializer.data)

    def post(self, request, blog_id):
        uid = request.user.uid
        comment = request.POST.get('comment')
        parent = request.POST.get('parent_id')

        result = helper.create_blog_comment(uid, blog_id, parent, comment)
        return SuccessResponse({'success': result})


class FollowerAPIView(ProtectedBaseAPIView):
    def get(self, request, uid):
        pass

