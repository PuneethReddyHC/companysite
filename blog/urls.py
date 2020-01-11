from . import views
from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
app_name = "blogs"
urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="blogs"),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]

