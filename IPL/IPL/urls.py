"""IPL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from api import views

from rest_framework.routers import DefaultRouter


#creating router object
router=DefaultRouter()
router.register('matchapi', views.MatchAPI,basename='match')
router.register('deliveryapi', views.DeliveryAPI,basename='delivery')


from api.api import fetchapi
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('up', views.simple_upload),

                  path('', views.MatchePlayed,name='MatchePlayed'),
                  path('2', views.MatchStackBar,name='MatchStackBar'),
                  path('3', views.ExtraRunConceded,name='ExtraRunConceded'),
                  path('4', views.EconomicalBowler,name='EconomicalBowler'),
                  path('5', views.MatchesPlayedWon,name='MatchesPlayedWon'),

                  path('fetch', fetchapi),

                  path('api/', include(router.urls)),
                  path('auth/', include('rest_framework.urls',namespace='rest_framework')),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
