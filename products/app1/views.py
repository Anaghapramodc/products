from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import product
from .serializer import ProductSerializer


# Create your views here.


@api_view(['Get'])
def api_overview(request):
    api_urls = {
        'list': '/product/list',
        'detail view': '/product/details/<intt:id>',
        'create': '/product/create/',
        'delete': '/product/delete/<int:id>',
        'update': '/product/update/<int:id>',
    }

    return Response(api_urls)


# list
@api_view(['Get'])
def showall(request):
    products = product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# create
@api_view(['Post'])
def createproduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



#detailview
@api_view(['Get'])
def detailview(request, pk):
    products = product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['Post'])
def Updateview(request, pk):
    products = product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['Delete'])
def deleteview(request, pk):
    products = product.objects.get(id=pk)
    products.delete()
    return Response("The item is deleted")

