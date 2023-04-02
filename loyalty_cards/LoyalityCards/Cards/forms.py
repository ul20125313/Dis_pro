from django.forms import ModelForm
from .models import Card


class Gen_Card_Form(ModelForm):
    class Meta:
        model = Card
        fields = ['card_valid_date']


class Get_Cards(ModelForm):
    class Meta:
        model = Card
        fields = ['id', 'series', 'card_number',
                  'card_released', 'card_valid_date',
                  'card_status','card_transaction_amount','card_level_membership']
