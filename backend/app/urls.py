from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]
