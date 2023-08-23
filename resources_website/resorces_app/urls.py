"""resorces_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path]
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from resorces_app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', views.def_home, name='home'),
     path('about', views.def_about, name='about'),
     path('team', views.def_team, name='team'),
     path('contact', views.def_contact, name='contact'),
     path('pyq/<str:branch_name>', views.def_pyq, name='pyq_show'),
     path('pyq_year/<int:student_year>/<str:branch_name>', views.show_year, name='pyq_year'),
     path('pyq_year/<int:student_year>/<str:branch_name>/<int:year>', views.year_year, name='pyq_year'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
