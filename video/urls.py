from django.urls import path
from .import views
from video.views import categories,categoryviews



app_name='video'
urlpatterns=[
    # path('category/',views.categories.as_view(),name='category'),
    path('category/',categories.as_view(),name='category'),
    
    path('<slug:category_slug>/', categoryviews.as_view(),name='category_view'),
    # path('<str:article_slug>',ArticleDetails.as_view(),name='article_detail'),
    path('postComment',views.postComment,name='postComment'),
    path('<slug:article_slug>',views.article_detail,name='article_detail'),
    
    
    # path('<slug:category_slug>/',views.category_view, name='category_view'),



]