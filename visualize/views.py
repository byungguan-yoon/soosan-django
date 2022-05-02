from django.shortcuts import render, redirect
from visualize.models import Image, Labeling
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from visualize.forms import LoginForm
from rest_framework import viewsets

CLASS_LIST = ['01.정상조직(템퍼드 마르텐사이트)',
    '02.재측정 필요 (초점)', '03.재측정 필요 (부식)', '04.재측정 필요 (위치)', '05.재측정 필요 (스크레치)',
    '06.부적합 (탄화물 미량_특채)', '07.부적합 (탄화물_폐기)', '08.부적합 (잔류오스테나이트)', '09.부적합 (탈탄)']

def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        msg = "가입되어 있지 않거나 로그인 정보가 잘못 되었습니다."
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        return render(request, "login.html", {"form": form, "msg": msg})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("index")

def inspection_view(request):
    image = Image.objects.last()
    return render(request, "inspection.html", {"image": image})

def past_inspection_view(request, id):
    image = Image.objects.get(pk=id)
    return render(request, "inspection.html", {"image": image})

@login_required(login_url='login')
def list_view(request):
    method = request.GET.get("method", "created_date")
    class_num = int(request.GET.get("class_num", "1"))
    page = int(request.GET.get("p", 1))
    if method == "predicted_value":
        class_name = CLASS_LIST[class_num-1]
        print(class_name)
        image = Image.objects.filter(result__predict_9class=class_name).all().order_by("-created_at")
    elif method == "labeled_class":
        class_name = CLASS_LIST[class_num-1]
        print(class_name)
        image = Image.objects.filter(labeling__ground_Y=class_name).all().order_by("-created_at")
    else:
        if class_num == 1:
            image = Image.objects.all().order_by("-created_at")
        else:
            image = Image.objects.all().order_by("created_at")
    paginator = Paginator(image, 10)
    image = paginator.get_page(page)
    return render(request, "boards.html", {"image": image})

@login_required(login_url='login')
def labeling_view(request):
    unlabeled_image = Image.objects.filter(labeling__isnull=True).order_by("-created_at").first()
    unlabeled_images = Image.objects.filter(labeling__isnull=True).all().order_by("-created_at")
    if len(unlabeled_images) > 10:
        unlabeled_images = unlabeled_images[:10]
    return render(request, "labeling.html", {"image": unlabeled_image, "images":unlabeled_images, "class_list": CLASS_LIST})

@login_required(login_url='login')
def choice_labeling_view(request, id):
    unlabeled_image = Image.objects.get(pk=id)
    unlabeled_images = Image.objects.filter(labeling__isnull=True).all().order_by("-created_at")
    if len(unlabeled_images) > 10:
        unlabeled_images = unlabeled_images[:10]
    return render(request, "labeling.html", {"image": unlabeled_image, "images":unlabeled_images, "class_list": CLASS_LIST})

def annotation_view(request, id):
    new_labeling = Labeling()
    new_labeling.user_id = request.user.id
    new_labeling.ground_Y = request.POST['choice']
    new_labeling.save()

    update_labeling = Image.objects.get(id=id)
    update_labeling.labeling_id = new_labeling.id
    update_labeling.save()
    return HttpResponseRedirect(reverse("labeling"))
