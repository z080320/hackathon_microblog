from django.conf.urls import include, url
# from django.contrib import admin
from hackathon_microblog.microblog import views as microblog_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hackathon_microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^garena_oauth/', include('gtoext.contrib.garena_oauth.urls')),

    url(r'^$', microblog_views.ProtectedTemplateView.as_view(template_name='index.html')),

    url(r'^home/$', microblog_views.HomeBlogAPIView.as_view()),
    url(r'^microblog/(?P<uid>\d+)/$', microblog_views.MicroblogAPIView.as_view()),
    url(r'^comments/(?P<blog_id>\d+)/$', microblog_views.CommentAPIView.as_view()),
    url(r'followers/(?P<uid>\d+)/$', microblog_views.FollowerAPIView.as_view()),
]
