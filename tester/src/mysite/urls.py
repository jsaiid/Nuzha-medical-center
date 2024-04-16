"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from watad.views import (home_view)

from watad.views import (contact_view ,activities_view,our_partners_view,strategy_view,presedent_lettre_view ,
                         calls_view,activity_view,newsActivity_view,details_job_view)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactUs',contact_view),
    path('',home_view),
    
     path('our_partners',our_partners_view),
      path('strategy',strategy_view ),
      path('presedent_lettre',presedent_lettre_view  ),
      path('calls',calls_view ),
        path('activities',activities_view),
       path('activity',activity_view ),
       path('newsactivity',newsActivity_view),
         path('calls',calls_view),
         path('details_job',details_job_view),



]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
