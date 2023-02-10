from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>', views.supers_detail),
    path('<path:type>',views.supers_list,name='type_param')
]
