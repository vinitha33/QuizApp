from django.urls import path
from . import views


urlpatterns=[
    path('Display',views.Display),
    path('Insert',views.Insert),
    path('Update/<str:pk>',views.Update),
    path('Delete/<str:pk>',views.Delete),
]