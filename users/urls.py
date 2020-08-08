from django.urls import path

from .views import LoginView, LogoutView, UserView

urlpatterns = [
	path('', UserView.as_view()),
	path('login/', LoginView.as_view()),
	path('logout/', LogoutView.as_view()),

]
