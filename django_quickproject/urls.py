"""
URL configuration for django_quickproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.api.views import UserProfileExampleViewSet
from users.api.register_apiview import RegistroUsuario
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import path
from users.api.register_apiview import LoginAPIView


router = SimpleRouter()

router.register("users", UserProfileExampleViewSet, basename="users")

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),   # Redireciona para a página de login
    path("admin/", admin.site.urls),
    path('api/', include('perguntas.urls')),
    path("api/token-auth/", views.obtain_auth_token),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('registro.html', TemplateView.as_view(template_name="registro.html"), name='registro_html'),  # URL para registro.html
    path('index__simulador.html', TemplateView.as_view(template_name="index__simulador.html"), name='simulador_html'),  # URL para simula.html
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('index_quest.html', TemplateView.as_view(template_name="index_quest.html"), name='index_quest'),  # URL para simula.html
    
]+router.urls
