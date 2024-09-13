from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendrier, name='calendrier'),
    path('api/presences/', views.get_presences, name='get_presences'),
    path('presence/<int:presence_id>/', views.presence_detail, name='presence_detail'),
]
