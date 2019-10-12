from django.contrib import admin
from django.conf.urls import url
from django.urls import  path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api.posts_api import NoteViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'posts', NoteViewSet)
router.register(r'userpost', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('feed.urls')),
    url(r'^', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
