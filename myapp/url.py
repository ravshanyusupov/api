from django.urls import path
from . import views

urlpatterns = [
    path('api', views.apiList),
    path('api/<str:pk>', views.apiDetail),
    path('api-create', views.apiCreate),
    path('api-update/<str:pk>', views.apiUpdate),
    path('api-delete/<str:pk>', views.apiDelete),

]