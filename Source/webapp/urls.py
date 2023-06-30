from django.urls import path

from webapp.views import todolist_view, todolist_detail, todolist_delete, todolist_create

urlpatterns = [
    path('', todolist_view, name='todolist'),
    path('detail/<int:pk>', todolist_detail, name='detail'),
    path('detail/<int:pk>/delete/', todolist_delete, name='delete'),
    path('create/', todolist_create, name='create')
]
