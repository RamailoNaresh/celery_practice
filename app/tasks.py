from celery import shared_task
import random
from .models import SumModel


@shared_task(name="adding_numbers")
def add_num():
    datas = SumModel.objects.filter(status="PENDING").first()
    print(datas)
    if datas:
        datas.sum = datas.num1 + datas.num2
        datas.status = SumModel.SUCCESS
        datas.save()
        return "saved"
