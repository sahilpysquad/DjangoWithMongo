from django.urls import path

from .views import MongoDBUserAPIView, PostgresUserAPIView, MixSearch

urlpatterns = [
    path("create-post-mongodb/", MongoDBUserAPIView.as_view(), name="user_create_in_mongodb"),
    path("create-post-postgres/", PostgresUserAPIView.as_view(), name="user_create_in_postgres"),
    path("search/", MixSearch.as_view(), name="search"),
]
