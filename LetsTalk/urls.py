from . import views
from django.urls import path
# from .views import booking_view
urlpatterns = [
    path('', views.index,name='index'),
    path('questions/', views.questions_page, name='questions_page'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
]