
HACKATHON_MICROBLOG = {
    getCookie: function(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },

    microblog_template: '<!--个人展示-->\
                <div class="stateShow">\
                  <div class="stateShowWord">\
                    <table width="450" border="0" cellpadding="0" cellspacing="0" class="stateTable">\
                      <tr>\
                        <td width="70" align="center" valign="top"><a href="#"><img src="/static/images/garena_avatar.png" width="54" height="54" alt="" title="" /></a></td>\
                        <td width="380"><a class="user" href="#">开心段子微博</a><div class="microblog"></div></td>\
                      </tr>\
                    </table>\
                  </div>\
                   <div class="stateImgShow"></div>\
                  <div class="stateShowtime"></div>\
                  <div class="stateOp"><a onclick="reXianShi(this)" class="opState">Reply</a><a class="opState">Repost</a><a class="opState" onclick="delState(this)">Delete</a></div>\
                  <div class="huifu"></div>\
                </div>\
                 <!--个人展示结束-->',

    comment_template: '<div class="comment">\
        <div class="username"></div>\
        <div class="replyTo"></div>\
        <div class="content"></div>\
        <div class="comment_time"></div>\
    </div>',

    load_blog: function(blog, $target_div){
        var that = this;
        var blog_tmpl = $(that.microblog_template);
        blog_tmpl.find('.microblog').html(blog.blog).end()
                 .find('.stateShowtime').html(blog.blog_post_time).end()
                 .find('.user').html('Garena '+ blog.uid);

        $.get('/comments/'+ blog.id +'/', function(comments){
            $target_region = blog_tmpl.find('.huifu');
            $.each(comments, function(index, comment){
                var comment_tmpl = $(that.comment_template);
                var replyTo = '';
                if (comment.parent_uid){
                    replyTo = 'Reply to Garena ' + comment.parent_uid;
                }
                comment_tmpl.find('.username').html('Garena ' + comment.uid).end()
                            .find('.replyTo').html(replyTo).end()
                            .find('.content').html(comment.blog).end()
                            .find('.comment_time').html(comment.blog_post_time);
                comment_tmpl.appendTo($target_region);
            });
        });
        
        blog_tmpl.appendTo($target_div);
    },

    load_home_blogs: function(){
        var that = this,
            home_microblogs = $('.home_microblogs');
        home_microblogs.html('');
        $.get('/home/', function(blogs){
            $.each(blogs, function(index, blog){
                that.load_blog(blog, home_microblogs);
            });
        });
    },

    post_microblog: function(blog){
        $.ajax({
            method: 'POST',
            url: '/home/',
            headers: {
                'X-CSRFToken': this.getCookie('csrftoken')
            },
            data: {
                'blog': blog 
            },
            success: function(ret){
                if(ret.success){
                    alert('Microblog post successfully!');
                }

                return false;
            }
        });
    }, 

    load_blog_comments: function(blog_id){
        $.get('/comments/'+blog_id+'/', function(comments){
            $.each(comments, function(index, comment){
                window.console.log(comment);
            });
        });
    },

    post_blog_comment: function(blog_id, comment, parent_id){
        $.ajax({
            method: 'POST',
            url: '/comments/'+ blog_id + '/',
            headers: {
                'X-CSRFToken': this.getCookie('csrftoken')
            },
            data: {
                'comment': comment,
                'parent_id': parent_id, 
            },
            success: function(ret){
                if(ret.success){
                    alert('Microblog comment post successfully!');
                    HACKATHON_MICROBLOG.load_home_blogs();
                }

                return false;
            }
        });
    }
};


$(document).ready(function(){
    $('#submit_microblog').on('click', function(){
        var blog = $('#mainBannerTopIssueFrame textarea').val();
        window.console.log(blog);

        HACKATHON_MICROBLOG.post_microblog(blog);
        
        return false;
    });


    HACKATHON_MICROBLOG.load_home_blogs();
    // HACKATHON_MICROBLOG.post_microblog('Microblog posting test!');
});