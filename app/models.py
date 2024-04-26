from django.db import models

# Create your models here.


class SumModel(models.Model):
    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    STATUS = [
        (PENDING, "PENDING"),
        (FAILED, "FAILED"),
        (SUCCESS, "SUCCESS")
    ]

    num1 = models.PositiveIntegerField(default=0)
    num2 = models.PositiveIntegerField(default=0)
    sum = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default=PENDING, max_length=100)
