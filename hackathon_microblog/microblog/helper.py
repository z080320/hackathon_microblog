from hackathon_microblog.microblog import models
import datetime


def get_user_recent_blog(uid):
    recent_blogs = models.Microblog.objects.filter(uid=uid).order_by('-post_time')[:20]
    return recent_blogs

def get_user_followers(uid):
    followers = models.Follower.objects.filter(uid=uid)
    return followers


def get_followee_recent_blog(uid):
    followees = models.Follower.objects.filter(follower_uid=uid)
    follower_uids = [followee.uid for followee in followees]
    follower_uids.append(uid) # Append self uid

    recent_blogs = models.Microblog.objects.filter(uid__in=follower_uids).order_by('-post_time')[:20]
    return recent_blogs

def post_microblog(uid, blog):
    models.Microblog.objects.create(uid=uid,
                            blog=blog,
                            post_time=datetime.datetime.now())


def get_blog_comments(uid, blog_id):
    try:
        blog = models.Microblog.objects.get(pk=blog_id)
        comments = models.Comment.objects.filter(comment_blog=blog).order_by('post_time')[:100]

        return comments

    except models.Microblog.DoesNotExist:
        return None


def create_blog_comment(uid, blog_id, parent, comment):
    try:
        blog = models.Microblog.objects.get(pk=blog_id)
        parent_comment = None
        if parent:
            try:
                parent_comment = models.Comment.objects.get(pk=parent)
            except models.Comment.DoesNotExist:
                pass

        models.Comment.objects.create(uid=uid,
                                      blog=comment,
                                      post_time=datetime.datetime.now(),
                                      comment_blog=blog,
                                      parent=parent_comment)
        return True

    except models.Microblog.DoesNotExist:
        return False

        
