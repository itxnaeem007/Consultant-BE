from django.urls import path
from service import views


urlpatterns = [
    path('list',views.ServiceListView.as_view(),name='service_list'),
]
