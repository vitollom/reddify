from django.urls import path
from spotify import views

urlpatterns = [
	path('connect/', views.connect_spotify),
	path('callback/', views.callback_action),
	path('refresh_token/', views.refresh_token),
]
