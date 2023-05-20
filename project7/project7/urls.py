"""
URL configuration for project7 project.

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
from django.urls import path,include
from app7 import views

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.base,name='base'),
    path('login1/',views.user_login1,name='login1'),
    path('logout1/',views.user_logout1,name='logout1'),
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('signup/',views.signup1,name='signup1'),
    path('view/',views.view,name='view'),
    path('add/',views.add,name='add'),
    
    path('delete/<int:p>',views.delete_emp,name='delete_emp'),
    path('edit/<int:p>',views.edit_emp,name='edit_emp'),

]
