
from django.urls import path
from .views import signup, activate_email

urlpatterns = [
	path('register/', signup, name='register'),
	path("activate/<slug:uidb64>/<slug:token>/", activate_email, name="activate"),
]