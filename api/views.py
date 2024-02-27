from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action 

from api.serializers import EmployeeSerializer
from api.models import Employees

# Create your views here.

class EmployeeViewSetView(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(qs)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employobject=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(data=request.data,instance=employobject)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return Response(data={"message":"employee was deleted"})


# list,retrieve,update,destroy

class EmployeeModelViewSetView(viewsets.ModelViewSet):

    serializer_class=EmployeeSerializer
    model=Employees
    queryset=Employees.objects.all()

    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        if "department" in request.query_params:
            value=request.query_params.get("department")
            qs=qs.filter(department=value)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    @action(methods=["get"],detail=False)
    def departments(self,request,*args,**kwargs):
        data=Employees.objects.all().values_list("department",flat=True).distinct()
        return Response(data=data)


