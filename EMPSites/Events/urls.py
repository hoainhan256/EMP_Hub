from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ( 
    EventCategoryCreateView,
    EventCategoryUpdateView,
    EventCategoryDeleteView,
    category_list,
    profile_view
    )


urlpatterns = [
path('create-category/', EventCategoryCreateView.as_view(), name='create_event_category'),
path('category-list/', category_list, name='event_category_list'),
path('category/<int:pk>/edit/', EventCategoryUpdateView.as_view(), name='edit_event_category'),
path('category/<int:pk>/delete/', EventCategoryDeleteView.as_view(), name='delete_event_category'),
path('profile-form/', profile_view, name='profile_form'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)