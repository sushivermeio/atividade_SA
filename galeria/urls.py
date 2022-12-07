from django.urls import path, include
from galeria.views import index, cadastro, loginuser, logoutuser

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
]
