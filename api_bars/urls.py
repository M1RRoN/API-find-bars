"""api_bars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import rest_framework
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter


from api_bars.views import index, SearchView, CreateUserView
from categories.views import CategoryViewSet
from establishments.views import PlaceViewSet
from reviews.views import ReviewViewSet

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', index, name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('register/', CreateUserView.as_view(), name='register'),

    # path('auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken'))
]
