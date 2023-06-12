from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('create/', views.WinPostCreateView.as_view(), name = 'office-create'),
    path('', views.PostListView.as_view(), name = 'office-index'),
    path('done/<int:pk>/', views.PostDoneListView.as_view(), name = 'office-index-done'),
    path('sort/', views.PostSortView.as_view(), name = 'office-sort'),
    path('sorted/<int:pk>/<int:customer>/<int:company>', views.OfiiceSortedListView.as_view(), name = 'office-sort'),
    path('wincreate/', views.PostCreateView.as_view(), name = 'win-office-create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='office-update'),
    path('<int:pk>/detail/', views.PostDetailView.as_view(), name='office-detail'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='office-delete'),

    path('customer/', views.CustomerListView.as_view(), name = 'customer-index'),
    path('customer/create/', views.CustomerCreateView.as_view(), name = 'customer-create'),
    path('customer/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),

    path('customer/<int:pk>/projects/', views.CustomerProjectListView.as_view(), name='customer-project-list'),

    path('material/', views.MaterialListView.as_view(), name = 'material-index'),
    path('material/create/', views.MaterialCreateView.as_view(), name = 'material-create'),
    path('material/<int:pk>/update/', views.MaterialUpdateView.as_view(), name='material-update'),
    path('material/<int:pk>/delete/', views.MaterialDeleteView.as_view(), name='material-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)