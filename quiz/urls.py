from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quiz_id>/', views.detail, name = 'detail'),
    path('<int:quiz_id>/quiz_list/', views.quiz_list, name='quiz_list'),
]
