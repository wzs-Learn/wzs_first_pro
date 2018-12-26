from django.urls import path

from Web_service import views

from django.contrib import admin

urlpatterns = [
   # path('hello/', view.hello),
    path('admin/', admin.site.urls),
    path('', views.index),   # 添加views.index 
   #path('world/', view.world)
]
