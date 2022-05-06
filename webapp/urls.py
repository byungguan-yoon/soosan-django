from visualize.views import index, login_view, logout_view, list_view, labeling_view, annotation_view, inspection_view, past_inspection_view, choice_labeling_view, dataset_view, make_dataset_view, train_view, aimodel_view, set_aimodel_view
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ninja import NinjaAPI
from visualize.images.apis import router as image_router

api = NinjaAPI(title = "Soosan API")
api.add_router("/images/", image_router, tags=["Common"])

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("ninja-api/", api.urls),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("inspection/", inspection_view, name="inspection"),
    path("inspection/<int:id>", past_inspection_view, name="past_inspection"),
    path("list", list_view, name="list"),
    path("labeling", labeling_view, name="labeling"),
    path("labeling/<int:id>", choice_labeling_view, name="choice_labeling"),
    path("annotation/<int:id>", annotation_view, name="annotation"),
    path("dataset", dataset_view, name="dataset"),
    path("make-dataset", make_dataset_view, name="make_dataset"),
    path("train", train_view, name="train"),
    path("aimodel", aimodel_view, name="aimodel"),
    path("set-aimodel", set_aimodel_view, name="set_aimodel"),
]
