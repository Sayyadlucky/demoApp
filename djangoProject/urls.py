from django.contrib import admin
from django.urls import path,include
from app1 import views
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
router = DefaultRouter()
router.register("studentapi",views.StudData,basename="studapi")

urlpatterns = [
    path("api1",include(router.urls)),
    path('admin/', admin.site.urls),
    path("",csrf_exempt(views.index))

]
