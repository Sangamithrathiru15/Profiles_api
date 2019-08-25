from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profile_api import views

router=DefaultRouter()#assign the router to a variable
router.register('hello-viewset',views.HelloViewSet,base_name="hello-view-set")#nam of the url,#the view set that needs to be registered
#to register specific viewset with the router
router.register('profile',views.UserProfileViewset)#base_name is not required since queryset was usedfor retrieving the values since the values in the query set will have the names, if we wish to overwrite then base_name can be defined
router.register('feed',views.UserProfileFeedItemViewset)

urlpatterns=[
path('hello-view/',views.HelloApiView.as_view()),#as_view is the function(class method) which will connect my MyView class with its url.
path('login/',views.UserLoginAPIView.as_view()),
path('',include(router.urls)),
]
