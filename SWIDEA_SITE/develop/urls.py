from django.urls import path
from .views import *

app_name = "develop"

urlpatterns = [
    path('', list_idea, name="list_idea"),

    path('tools', list_tool, name="list_tool"),
    path('create/tool', create_tool, name="create_tool"),
    path('tool/<int:pk>', show_tool, name="show_tool"),
    path('edit/tool/<int:pk>', edit_tool, name="edit_tool"),
    path('delete/tool/<int:pk>', delete_tool, name="delete_tool"),

    path('create/idea', create_idea, name="create_idea"),
    path('idea/<int:pk>', show_idea, name="show_idea"),
    path('edit/idea/<int:pk>', edit_idea, name="edit_idea"),
    path('delete/idea/<int:pk>', delete_idea, name="delete_idea"),

    path('interest/', edit_interest, name="interest")
]