from django.urls import path

from .views import ( 
    EventCategoryCreateView,
    category_list 
    )


urlpatterns = [
path('create-category/', EventCategoryCreateView.as_view(), name='create-event-category'),
path('category-list/', category_list, name='event-category-list'),
]