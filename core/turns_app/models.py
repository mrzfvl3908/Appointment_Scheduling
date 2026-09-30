from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class ReservationDay(models.Model):
    date = models.DateField(_('Date'), unique=True)

    class Meta:
        verbose_name = _('Reservation Day')
        verbose_name_plural = _('Reservation Days')
        ordering = ['-date']

    def __str__(self):
        return str(self.date)


class Reservation(models.Model):
    day = models.ForeignKey(ReservationDay, on_delete=models.CASCADE, verbose_name=_('Day'),
                            related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=_('User'), null=True, blank=True,
                             related_name='reservations')
    time = models.TimeField(_('Time'))

    class Meta:
        verbose_name = _('Reservation')
        verbose_name_plural = _('Reservations')
        ordering = ['-time']
        constraints = [
            models.UniqueConstraint(fields=['user', 'day','time'], name='unique_reservation_day_time')
        ]

    def __str__(self):
        return f'{self.user} - {self.day} - {self.time}'
