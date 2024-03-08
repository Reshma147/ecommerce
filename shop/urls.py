from django.contrib import admin
from django.urls import path
from shop import views

from django.conf import settings
from django.conf.urls.static import static
app_name="shop"
urlpatterns = [
    path('', views.allcategories, name="allcat"),
    path('allpord/<p>',views.allproducts,name="allprod"),
    path('details/<c>',views.details,name="details",),
    path('register',views.register,name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
