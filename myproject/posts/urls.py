from django.conf.urls import patterns, include, url

from posts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.getposts_from_model, name='index'),
    url(r'^(?P<postid>\d+)', views.getposts_from_model_by_id,),
    url(r'^new/', views.post_form,),
    url(r'^comments/new/(?P<postid>\d+)', views.comments_form,),
    url(r'^user/(?P<userid>\d+)', views.getuser, ),
)
