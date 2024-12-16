from django.urls import path
from .views import index, TutorialListView, SearchTemplateView, CategoryCreateView, CategoryDeleteView, \
    CategoryDetailView, TutorialCreateView, TutorialDetailView, TutorialDeleteView, CategoryUpdateView, \
    TutorialUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/category', CategoryDetailView.as_view(), name='detail-category'),
    path('create/category', CategoryCreateView.as_view(), name='create-category'),
    path('<int:pk>/category/update', CategoryUpdateView.as_view(), name='update-category'),
    path('<int:pk>/category/delete', CategoryDeleteView.as_view(), name='delete-category'),
    path('<int:pk>/category/tutorials', TutorialListView.as_view(), name='list-tutorial'),
    path('<int:pk>/category/<int:pkt>/tutorial', TutorialDetailView.as_view(), name='detail-tutorial'),
    path('<int:pk>/category/<int:pkt>/tutorial/update', TutorialUpdateView.as_view(), name='update-tutorial'),
    path('<int:pk>/category/<int:pkt>/tutorial/delete', TutorialDeleteView.as_view(), name='delete-tutorial'),
    path('<int:pk>/category/create/tutorial', TutorialCreateView.as_view(), name='create-tutorial'),
    path('search', SearchTemplateView.as_view(), name='search'),
]
