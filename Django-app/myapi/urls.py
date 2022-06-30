from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('my api', views.approvalView)
urlpatterns = [
    path('', views.home, name='home'),
    path('calculator/', views.cxcontact, name="cxform"),
    path('api/', include(router.urls)),
    path('status/', views.approveReject),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
]