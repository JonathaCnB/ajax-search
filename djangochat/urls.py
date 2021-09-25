from django.urls import path

from .views import check_view, get_messages_view, send_view, to_enter, view_room

urlpatterns = [
    path("", to_enter, name="to_enter"),
    path("check-room/", check_view, name="checkview"),
    path("send/", send_view, name="send"),
    path("get_messages/<str:room>/", get_messages_view, name="get_messages"),
    path("<str:room>/", view_room, name="room"),
]
