from django.urls import path
from .views import homePageView

urlpatterns=[
    path('',homePageView,name='home')
]

# path(regex,reference to the view,optional named URL pattern)