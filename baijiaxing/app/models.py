from django.db import models

# Create your models here.

class Baijiaxing(models.Model):
    id = models.IntegerField(primary_key=True)
    xingshi = models.CharField(max_length=256)
    href = models.CharField(max_length=1024)
    xingshi_zhongwen = models.CharField(max_length=256)

    class Meta:
        db_table = "baijiaxing"

class Xingming(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    the_same_people_number = models.CharField(max_length=256)
    boy_ratio = models.CharField(max_length=256)
    girl_ratio = models.CharField(max_length=256)
    five_elements = models.CharField(max_length=256)
    three_talents = models.CharField(max_length=256)
    xingshi = models.ForeignKey(Baijiaxing)

    class Meta:
        db_table = 'xingming'
