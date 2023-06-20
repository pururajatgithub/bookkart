from django.core.management.base import BaseCommand
from django.urls import path, include
from rest_framework import routers
from book.views import MyBookViewSet, MyBookViewList
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from book.views import Contact
router = routers.DefaultRouter()

router.register(r'book', MyBookViewSet)
router.register(r'book/id', MyBookViewList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('contact/',Contact,name='contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)