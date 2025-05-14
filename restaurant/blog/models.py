from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


class Blog (models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    discription = models.CharField(_("توضیحات"), max_length=100)
    content = RichTextField()
    created_at = models.DateTimeField(_("تاریخ انتشار"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to="blogs/", blank = True , null = True)
    category = models.ForeignKey("Category", related_name="blog", verbose_name=_("دسته بندی"), on_delete=models.CASCADE, blank = True , null = True)
    tags = models.ManyToManyField("Tag", verbose_name=_("تگ ها"),related_name="blogs", blank = True , null = True)
    def __str__(self):
        return self.title

class Category (models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    blog = models.ForeignKey("blog", related_name="comments", verbose_name=_("مقاله"), on_delete=models.CASCADE, blank = True , null = True)
    name = models.CharField(_("نام کاربر"), max_length=50)
    email = models.EmailField(_("پست الکترونیکی"), max_length=100)
    message = models.TextField(_("متن"))
    date = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.email