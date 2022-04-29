from visualize.views import index, login_view, logout_view, list_view, labeling_view, annotation_view, inspection_view, past_inspection_view, choice_labeling_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("inspection/", inspection_view, name="inspection"),
    path("inspection/<int:id>", past_inspection_view, name="past_inspection"),
    path("list", list_view, name="list"),
    path("labeling", labeling_view, name="labeling"),
    path("labeling/<int:id>", choice_labeling_view, name="choice_labeling"),
    path("annotation/<int:id>", annotation_view, name="annotation"),
]
