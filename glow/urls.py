from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    url('^$',views.home,name='home'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^category/(\w+)', views.page_category,name='page_category'),
    url('^uploads/',views.post_routine,name='post_routine'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    