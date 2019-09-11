from django.urls import path
from . import views

urlpatterns = [
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('accueil', views.home),
    path('article/<int:id_article>', views.view_article),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
]
