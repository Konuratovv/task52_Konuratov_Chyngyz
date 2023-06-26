from django.urls import path

from webapp.views import todolist_view, todolist_detail, todolist_delete, todolist_create

urlpatterns = [
    path('', todolist_view),
    path('detail/', todolist_detail),
    path('detail/delete/', todolist_delete),
    path('create/', todolist_create)
]
