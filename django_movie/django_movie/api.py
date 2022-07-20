from email.mime import base
from rest_framework import routers
from mov import views

router = routers.DefaultRouter()
router.register(r'homiyariza',views.UserViewSet, basename='homiyariza')
router.register(r'tushgan-arizalar', views.ArizaRuyhat, basename='tushgan-arizalar')
router.register(r'talaba_qushish', views.TalabaQushishView,basename='talaba_qushish')
router.register(r'talabaga_homiy_qushish', views.TalabaHomiyqushish, basename='talabaga_homiy_qushish')
router.register(r'Dashboard', views.DashboardView,basename='Dashboard')


