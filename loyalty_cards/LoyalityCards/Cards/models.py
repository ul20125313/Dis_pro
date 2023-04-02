from django.db import models
from django.utils import timezone

VISA = 'Visa'

CHOICE_VD = ((12, 'Card for 12'), (6, 'Card for 6'), (1, 'Card for 1'))
LEVEL = ((1, 'bronze'), (2, 'gold'), (3, 'platinum'))


class Card(models.Model):
    series = models.CharField(
        max_length=10,
        default=VISA,
    )
    card_number = models.CharField(max_length=16)
    card_released = models.DateTimeField(default=timezone.now)
    card_valid_date = models.IntegerField(choices=CHOICE_VD)
    card_use_date = models.DateTimeField(default=timezone.now)
    card_balance = models.IntegerField(default=0)
    card_status = models.BooleanField(default=False)
    card_transaction_amount = models.IntegerField(default=0)
    card_level_membership = models.IntegerField(choices=LEVEL, default= 1)
