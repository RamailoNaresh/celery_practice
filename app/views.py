from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import SumModel
from .serializers import SumSerializer


@api_view(["POST"])
def addingNum(request):
    data = request.data
    serializer = SumSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": f"Output is in {serializer.data.get('status')} state"})
    return JsonResponse({"message": serializer.errors})


@api_view(["GET"])
def getallObj(request):
    data = SumModel.objects.all()
    serializer = SumSerializer(data, many=True)
    return JsonResponse({"data": serializer.data})
