from django.urls import path
from blog import views


urlpatterns = [
    path('list',views.PostListView.as_view(),name="post_list"),
    path('create/',views.PostCreateView.as_view(),name='post-create'),
    path('update/<int:pk>',views.PostUpdateView.as_view(),name='post-update'),
    path('detail/<int:pk>',views.PostRetrieveView.as_view(),name='post-detail'),
    path('delete/<int:pk>',views.PostDeleteView.as_view(),name='post-delete'),
    path('author/list',views.AuthorListView.as_view(),name='author-list'),
    path('author/blogs/<int:pk>',views.AuthorBlogListView.as_view(),name='author-blogs')
]
