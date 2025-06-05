"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name= 'homepage' ),
    path('medicinedetail/<int:id>/', meddetail, name= 'meddetail'),
    path('emedicinelist/<int:id>/', emedlist, name= 'medlist'),
    path('diseaseupdateview/<int:id>/', dis_updateview, name= 'dis_updateview'),
    path('diseaseview/', dis_view, name= 'diseaseview'),
    path('adddisease/', adddisease, name= 'adddisease'),

    path('shop_view/', shop_view, name= 'shop_view'),
    path('addproduct/', addproduct, name= 'addproduct'),
    path('deleteitem/<int:id>', deleteitem, name= 'deleteitem'),
    path('deletedisease/<int:id>', deletedisease, name= 'deletedisease'),

    path('cartview/', cart_view, name= 'cart_view'),
    path('checkout/', checkout, name= 'checkout'),
    path('register/', register_view, name= 'register'),
    path('loginview/', loginView, name= 'loginView'),
    path('homeview/', HomeView.as_view(), name= 'homeview'),
    path('medview/', medview, name= 'medview'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
