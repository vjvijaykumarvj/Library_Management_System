from django.urls import path
from .import views


urlpatterns=[
    path('register/',views.Register),
    path('login/',views.Login),
    path('logout/',views.Logout),
]