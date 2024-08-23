"""
URL configuration for sentiment_nwt_project project.

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
from django.urls import path
from ESA import views as esa_views
from ESA1 import views as esa1_views
from ESA2 import views as esa2_views
from ESA3 import views as esa3_views
from ESA4 import views as esa4_views
from ESA5 import views as esa5_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', esa_views.email_sentiment_analysis, name='analyze_email'),
    path('data/', esa_views.email_list, name='email_list'),
    path('es/', esa1_views.esa1, name='esa1'),
    path('es2/',esa2_views.esa2, name='esa2'),
    path('es3/',esa3_views.esa3, name='esa3'),
    path('es4/',esa4_views.esa4,name='esa4'),
    path('es5/',esa5_views.esa5,name='esa5'),

    
]
