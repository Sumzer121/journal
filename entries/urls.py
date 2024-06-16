# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.journal_list, name='entries_list'),
    path('login/', views.custom_login_view, name='costom_login'),
    path('entries/<int:entry_id>/', views.journal_entry_detail, name='entry_detail')
    # Other URL patterns for authentication, editing entries, etc.
]
