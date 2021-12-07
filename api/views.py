from django.shortcuts import render
from .serializers import articalSerializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Artical
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ArticleAPIView(APIView):
    
    def get(self, request):
        articals = Artical.objects.all()
        serialzer = articalSerializers(articals, many = True)
        return Response(serialzer.data)

    def post(self, request):    
        serializer = articalSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# @csrf_exempt
# def artical_list(request):
#     if request.method == 'GET':
#         articals = Artical.objects.all()
#         serialzer = articalSerializers(articals, many = True)
#         return JsonResponse(serialzer.data, safe = False)

#     elif  request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = articalSerializers(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)    

@api_view(['GET','POST'])
def artical_list(request):
    if request.method == 'GET':
        articals = Artical.objects.all()
        serialzer = articalSerializers(articals, many = True)
        return Response(serialzer.data)

    elif  request.method == 'POST':
        serializer = articalSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# # @api_view(['GET','PUT','DELETE'])
# def article_detail(request, pk):
#     try:
#         article = Artical.objects.get(pk=pk)

#     except Artical.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = articalSerializers(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = articalSerializers(article,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)  
    

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)


@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
    try:
        article = Artical.objects.get(pk=pk)

    except Artical.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = articalSerializers(article)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = articalSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
