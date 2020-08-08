from django.contrib import admin
from django.urls import path, include

from users import urls as UsersUrls

urlpatterns = [
	path('user/', include(UsersUrls)),
    path('admin/', admin.site.urls),
]
