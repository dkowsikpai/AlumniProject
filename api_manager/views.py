from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.generics import ListAPIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .serializer import PostsSerializer
from forum.models import Posts

from PIL import Image

# Create your views here.


class PostApiManager(APIView):
    permission_classes = []
    authentication_classes = []
    parser_classes = [JSONParser, MultiPartParser]

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        posts = Posts.objects.filter(display=True)
        serializer_data = PostsSerializer(posts, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)

    @method_decorator(csrf_exempt)
    def put(self, request, format=None):
        # print(request.data)
        try:
            # if isinstance(request.data, dict):
            #     data = {'title': request.data['title'], 'id': request.data['id']}
            # else:
            #     data = {'title': request.data[0]['title'], 'id': request.data[0]['id']}
            # post = Posts.objects.get(id=data['id'])
            # post.title = data['title']
            # post.save()
            snippet = Posts.objects.get(id=request.data['id'])
            event = PostsSerializer(snippet, data=request.data, partial=True)  # TODO: Update not working
            if event.is_valid():
                print(event.validated_data)
                event.save()
                return Response({'received data': request.data, "is_done": True}, status=status.HTTP_200_OK)
            else:
                return Response("Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({"is_done": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        print(request.data)
        image = request.data['image1']
        try:
            img = Image.open(image)
            img.verify()
        except:
            print("Unsupported image type")

        event = PostsSerializer(data=request.data, partial=True)
        # event.save()
        if event.is_valid():
            event.save()
            return Response({'received data': request.data, "is_done": True}, status=status.HTTP_200_OK)
        else:
            return Response("Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
