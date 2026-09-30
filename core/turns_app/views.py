from django.http import HttpResponse
from django.shortcuts import render
from turns_app.utils.turn_maker import create_reservations


def home(request):
    create_reservations()
    return HttpResponse('Done')
