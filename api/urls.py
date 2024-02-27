from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router=DefaultRouter()
router.register("v1/employees",views.EmployeeViewSetView,basename="employess")
router.register("v2/employees",views.EmployeeModelViewSetView,basename="memployees")


urlpatterns=[
    
]+router.urls