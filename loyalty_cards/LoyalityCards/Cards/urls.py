from django.urls import path
from .views import (generator_card, get_all_cards, get_card,
                    change_status_card, delete_card, update_card_tran)

urlpatterns = [
    path('', get_all_cards, name='get_all_cards'),
    path('gen-card/', generator_card, name='gen_card'),
    path('<int:card_id>/', get_card, name='get_card'),
    # path('filter/', filter_card, name='filter'),
    path('<int:card_id>/change-status/',
         change_status_card, name='change_status'),
    path('<int:card_id>/delete/', delete_card, name="delete_card"),
    path('<int:card_id>/update_card/', update_card_tran, name='update_card')
]
