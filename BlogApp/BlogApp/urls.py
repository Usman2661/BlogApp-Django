from django.contrib import admin
from django.conf.urls import url
from django.urls import  path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api.posts_api import NoteViewSet, UserViewSet
from api.comment_api import CommentViewSet
from rental.rental_api import BelongingViewSet,BowrrowedViewSet,FriendViewSet
# from rental.api_views import BelongingViewset,BorrowedViewset,FriendViewset


router = routers.DefaultRouter()
router.register(r'posts', NoteViewSet)
router.register(r'userpost', UserViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'friends', FriendViewSet,basename='Friend')
router.register(r'belongings', BelongingViewSet)
router.register(r'borrowings', BowrrowedViewSet)

# router.register(r'borrowings/', MyModelView, basename='MyModel')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('feed.urls')),
    url(r'^', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    # path('api/v1/', include(router.urls)),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
