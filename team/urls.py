from django.urls import path
from team import views

urlpatterns = [
    path('list',views.TeamListView.as_view(),name='team_list'),
]
