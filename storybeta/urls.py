from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from storybeta import views as storybetaviews
from storybeta.views import StoryViewSet, UserViewSet,IterationViewSet, CommentViewSet

router = routers.DefaultRouter()
###router.register(r'api/',storybetaviews)
router.register(r'Stories', StoryViewSet)
router.register(r'Users', UserViewSet)
router.register(r'Iterations', IterationViewSet)
router.register(r'Comments', CommentViewSet)

urlpatterns = [
    
]
urlpatterns += router.urls