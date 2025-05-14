from django.db import models
from django.utils.translation import gettext as _

class Reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(_("پست الکترونیکی"), max_length=50)
    phone = models.IntegerField(_("شماره همراه"), max_length=13)
    number = models.IntegerField(_("تعداد"), max_length=50)
    date = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("ساعت"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

