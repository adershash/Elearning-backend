from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('courses',views.Course,basename='course')

urlpatterns=[
    # path('courses/',views.Course.as_view()),
    # path('courses/<int:pk>/',views.CourseDetails.as_view())
    path('',include(router.urls))
]