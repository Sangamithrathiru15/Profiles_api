from django.urls import path
from profile_api import views

urlpatterns=[
path('hello-view/',views.HelloApiView.as_view()),#as_view is the function(class method) which will connect my MyView class with its url.
]
