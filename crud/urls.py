from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from  .views import index ,  register , loginView , logout_view

urlpatterns = [
    path('', index ,  name  = 'index'),
    path('register/' , register , name  = 'register') ,
    path('login/' , loginView , name  = 'login' ),
    path('logout/' , logout_view , name='logout'),
    path('market/' ,  index ,  name = 'market')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)