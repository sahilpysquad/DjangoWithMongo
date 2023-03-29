from itertools import chain

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post


class MongoDBUserAPIView(APIView):

    def post(self, reqeust):
        name = reqeust.data.get("name")

        post_obj = Post(name=name)
        post_obj.save()
        return Response({"details": "Post Created Successfully in MongoDB Database."}, status=status.HTTP_200_OK)


class PostgresUserAPIView(APIView):

    def post(self, request):
        name = request.data.get("name")

        post_obj = Post(name=name)
        post_obj.save(using="users")
        return Response({"details": "Post Created Successfully in Postgres Database."}, status=status.HTTP_200_OK)


class MixSearch(APIView):

    def get(self, request):
        search_param = request.query_params.get("name")
        mongodb_queryset = Post.objects.all().values()
        postgres_queryset = Post.objects.all().using("users").values()
        queryset = chain(mongodb_queryset, postgres_queryset)
        if search_param:
            mongodb_queryset = Post.objects.filter(name=search_param).values()
            postgres_queryset = Post.objects.filter(name=search_param).using("users").values()
            queryset = chain(mongodb_queryset, postgres_queryset)
        return Response({"data": queryset}, status=status.HTTP_200_OK)
