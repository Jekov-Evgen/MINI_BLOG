from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comment'),
    path('review/<int:pk>/add_like', views.AddLike.as_view(), name='add_like'),
    path('review/<int:pk>/delete_like', views.AddDisLike.as_view(), name='del_like')
]
