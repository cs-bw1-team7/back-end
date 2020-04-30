from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name': player.user.username, 'title': room.title, 'description': room.description, 'players': players}, safe=True)


@api_view(["GET"])
def area(request):
    user = request.user
    player = user.player
    print(player.currentArea)
    area = Area.objects.get(id=player.currentArea)
    return JsonResponse({'width': area.width, 'height': area.height})


@api_view(["GET"])
def rooms(request):
    player = request.user.player
    rooms = Room.objects.filter(area=player.currentArea).values()
    return JsonResponse({'data': list(rooms)})


@api_view(["GET"])
def room(request):
    user = request.user
    player = user.player
    room = Room.objects.filter(
        area=player.currentArea).get(x=player.current_x, y=player.current_y)
    print(room)
    return JsonResponse({'Area': room.area.id, 'x': room.x, 'y': room.y, 'passable': room.passable})


# @csrf_exempt
@api_view(["POST"])
def move(request):
    user = request.user
    player = user.player
    x = player.current_x
    y = player.current_y
    direction = request.data["direction"]
    coord_shift = [0, 0]
    if direction == 'north':
        coord_shift[1] = 1
    if direction == 'south':
        coord_shift[1] = -1
    if direction == 'east':
        coord_shift[0] = 1
    if direction == 'west':
        coord_shift[0] = -1

    new_x = coord_shift[1] + x
    new_y = coord_shift[0] + y

    target_room = Room.objects.filter(
        area=player.currentArea).get(x=new_x, y=new_y)
    if target_room.passable:
        player.current_x = new_x
        player.current_y = new_y

        return JsonResponse({'name': player.user.username, 'room_x': target_room.x, 'room_y': target_room.y, 'error_msg': ""}, safe=True)
    else:
        return JsonResponse({'name': player.user.username, 'room_x': target_room.x, 'room_y': target_room.y, 'error_msg': "You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error': "Not yet implemented"}, safe=True, status=500)
