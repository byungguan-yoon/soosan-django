from typing import List
from visualize.schemas import Images as I
from visualize.models import Image, AI_Model, Data
from visualize.schemas import AI_Models as A
from visualize.schemas import AI_Models_Update, AI_Models_Update_Status
from visualize.schemas import Datasets as D
from ninja import Router
from visualize.utils import str2date
from collections import Counter
from django.shortcuts import get_object_or_404

router = Router()


@router.get("", response=List[I])
def get_image(request):
    a = Image.objects.all()
    return list(a)

@router.get("/bydate", response=List[I])
def get_image_bydate(request, startdate, enddate):
    startdate, enddate = str2date(startdate, enddate)
    a = Image.objects.filter(created_at__range=[startdate, enddate]).filter(labeling__isnull=False).all()
    return list(a)

@router.get("/bydate/statics")
def get_image_bydate(request, startdate, enddate):
    startdate, enddate = str2date(startdate, enddate)
    a = Image.objects.filter(created_at__range=[startdate, enddate]).filter(labeling__isnull=False).values_list('labeling__ground_Y', flat=True).all()
    cnt = dict(sorted(Counter(a).items()))
    return cnt

@router.get("/dataset/{id}", response=List[D])
def get_dataset(request, id):
    a = Data.objects.filter(pk=id)
    return list(a)   

@router.get("/ai-model/{id}", response=List[A])
def get_aimodel(request, id):
    a = AI_Model.objects.filter(pk=id)
    return list(a)

@router.patch("/ai-model/{id}")
def update_train(request, id, train_info: AI_Models_Update):
    ai_model = get_object_or_404(AI_Model, id=id)
    for attr,value in train_info.dict().items():
        setattr(ai_model,attr,value)
    ai_model.save()
    return {"message": f"successfully updated AI Model id: {id}"}

@router.patch("/ai-model/{id}/status")
def update_train(request, id, train_info: AI_Models_Update_Status):
    ai_model = get_object_or_404(AI_Model, id=id)
    for attr,value in train_info.dict().items():
        setattr(ai_model,attr,value)
    ai_model.save()
    return {"message": f"successfully updated AI Model's Status id: {id}"}