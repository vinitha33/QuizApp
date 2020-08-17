from django.urls import path
from . import views


urlpatterns=[
    path('Display',views.Display),
    path('Display_id/<int:pk>',views.Display_id),
    path('Insert',views.Insert),
    path('Update/<int:pk>',views.Update),
    path('Delete/<int:pk>',views.Delete),
    path('Login/',views.login),
    path('Login_id/<int:pk>',views.Login_id)
]

