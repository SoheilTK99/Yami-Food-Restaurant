from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="blog"

urlpatterns = [
    path("",views.blog_list,name="blog_list"),  
    path("<int:id>",views.blog_detail,name="blog_detail"),
    path("tag/<slug:tag>",views.blog_tag,name="tag"),
    path("category/<slug:category>",views.blog_category,name="category"),
    path("search/",views.search,name="search"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
