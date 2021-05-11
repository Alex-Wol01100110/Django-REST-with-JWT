from django.urls import path
from . import views

app_name = 'api_posts'

urlpatterns = [
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<pk>/like/', views.PostLikeView.as_view(), name='post_like'),
    path('post/<pk>/unlike/',
         views.PostUnlikeView.as_view(),
         name='post_unlike'),

    path('analitics/date_from=<date_from>date_to=<date_to>/',
         views.TotalLikesByDatesView.as_view(),
         name='total_likes_by_dates')
]
