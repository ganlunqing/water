from django.db import models

# Create your models here.

class WaterInfo(models.Model):
    num = models.SmallIntegerField(verbose_name="每次一杯水",default=1)
    start_time = models.DateTimeField(verbose_name="开始喝水", auto_now_add=True)
    end_time = models.DateTimeField(verbose_name="喝完一杯水")
    water = models.IntegerField(verbose_name='今日第几杯水', default=1)

class WaterPing(models.Model):
    '''提醒喝水'''
    time_choices = (
        (0, "9:30"),
        (1, "10:30"),
        (2, "13:30"),
        (3, "14:30"),
    )
