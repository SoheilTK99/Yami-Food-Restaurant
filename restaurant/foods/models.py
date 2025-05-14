from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Food(models.Model):
    FOOD_TYPE=[
        ("breakefast","صبحانه"),
        ("dinner","ناهار"),
        ("lunch","شام"),
        ("drinks","نوشیدنی"),
    ]
    name = models.CharField(max_length=100, default='Default Name')
    discription = models.CharField(_("توضیحات"), max_length=100)
    rate = models.IntegerField(("امتیاز"), default=0)
    time = models.IntegerField(("زمان پخت"), blank = True , null = True)
    price = models.IntegerField()
    pub_date = models.DateField(("زمان انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to='foods/', default='default.jpg')
    type_food = models.CharField(_("نوع غذا"),max_length=10,choices=FOOD_TYPE,default="drinks")
   
    def __str__(self):
        return self.name

   