from django.urls import path
from desarrollador import views

urlpatterns = [
    path('helloDesarrollador/', views.HelloAPIView.as_view()),
]

'/admin'
'http://127.0.0.1:8000/desarrollador/helloDesarrollador/'