from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Message, Room


def to_enter(request):
    return render(request, "djangochat/to_enter.html")


def view_room(request, room):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    context = {
        "username": username,
        "room": room,
        "room_details": room_details,
    }
    return render(request, "djangochat/room.html", context)


def check_view(request):
    if request.method == "POST":
        room = request.POST["room_name"]
        username = request.POST["username"]

        if Room.objects.filter(name=room).exists():
            return redirect("/chat/" + room + "/?username=" + username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect("/chat/" + room + "/?username=" + username)


def send_view(resquest):
    message = resquest.POST["message"]
    username = resquest.POST["username"]
    room_id = resquest.POST["room_id"]

    new_message = Message.objects.create(
        value=message,
        user=username,
        room=room_id,
    )
    new_message.save()
    return HttpResponse("Success")


def get_messages_view(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({"messages": list(messages.values())})
