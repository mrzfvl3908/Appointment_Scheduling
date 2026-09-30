from django.contrib import admin
from .models import Reservation, ReservationDay


class InlineReservation(admin.StackedInline):
    model = Reservation


@admin.register(ReservationDay)
class ReservationDayAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = [InlineReservation]