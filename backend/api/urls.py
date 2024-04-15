from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteListCreate.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', views.NoteDelete.as_view(), name='note-delete'),
    path('register/', views.CreateUserView.as_view(), name='register'),
]