from django.urls import path
from . import views

urlpatterns = [
    # path('article/',views.artical_list),
    path('details/<int:pk>',views.article_detail),
    path('articles/',views.ArticleAPIView.as_view()),
    
]