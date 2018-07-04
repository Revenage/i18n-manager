from django.urls import include, path
from .views import FacebookLogin, FacebookConnect

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/facebook/connect/',
         FacebookConnect.as_view(), name='fb_connect'),
    path('users/', include('users.urls')),
    path('documents/', include('documents.urls')),
]
