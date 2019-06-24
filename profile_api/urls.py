from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profile_api import views

router=DefaultRouter()#assign the router to a variable
router.register('hello-viewset',views.HelloViewSet,base_name="hello-view-set")#nam of the url,#the view set that needs to be registered
#to register specific viewset with the router

urlpatterns=[
path('hello-view/',views.HelloApiView.as_view()),#as_view is the function(class method) which will connect my MyView class with its url.
path('',include(router.urls)),
]
