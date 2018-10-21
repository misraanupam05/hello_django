from django.urls import path

from . import views
app_name ='blog'
urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    # ex: /blog/view/
    path('/blog/<slug>.html', views.view_post, name='view_post'),
    # ex: /polls/5/results/
    path('/cat/<slug>.html/', views.view_category, name='view_category'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
#(r'^$', 'djangorocks.blog.views.index'),
#url(
 #  r'^blog/view/(?P<slug>[^\.]+).html', 
  # 'djangorocks.blog.views.view_post', 
  # name='view_blog_post'),
#url(
#   r'^blog/category/(?P<slug>[^\.]+).html', 
#   'djangorocks.blog.views.view_category', 
#   name='view_blog_category'),
