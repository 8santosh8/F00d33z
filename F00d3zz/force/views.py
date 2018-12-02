from django.shortcuts import render
from django.http import HttpResponse
from .models import UserLog,EquationLog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from force.serializers import EquationLogSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

def index(request):
    return render(request,'force/index.html')

def result(request):
    fullname=request.POST['fullname']
    email=request.POST['email']

    userlog = UserLog.objects.create(fullname=fullname,email=email)
    mass1=request.POST['m1']
    position1=request.POST['x1']
    mass2=request.POST['m2']
    position2=request.POST['x2']
    com=((float(mass1) * float(position1)) + (float(mass2) * float(position2))) / (float(position1) + float(position2))
    context = {
        "com":com
    }
    EquationLog.objects.create(mass1=mass1,position1=position1,mass2=mass2,position2=position2,com=com,userlogid=userlog)
    return render(request,'force/result.html',context=context)

# @api_view()
# def equationloglist(request):
#     equationlogs=EquationLog.objects.all()
#     serializer=EquationLogSerializer(equationlogs,many=True)
#     return Response(serializer.data)

class EquationLogListView(APIView):
    def get(self,request):
        equationlogs = EquationLog.objects.all()
        serializer=EquationLogSerializer(equationlogs,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=EquationLogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)