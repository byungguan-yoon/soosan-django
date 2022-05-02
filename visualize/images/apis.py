from typing import List
from visualize.schemas import Images as I
from visualize.models import Image
from ninja import Router


router = Router()


@router.get("", response=List[I])
def get_image(request):
    a = Image.objects.all()
    return list(a)
