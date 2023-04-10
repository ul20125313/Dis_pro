from django.shortcuts import redirect, render, get_object_or_404
from .models import Card
from .forms import Gen_Card_Form, Get_Cards
from random import randint
from .kafkaproducer import send_message
from .kafkaconsumer import consume_messages
def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def get_all_cards(request):
    cards = Card.objects.all()
    context = {'cards': cards}
    return render(request, 'page_cards.html', context)


def generator_card(request):
    form = Gen_Card_Form()
    context = {'form': form}

    if request.method == 'POST':
        count = request.POST.get('count')
        card_valid_date = request.POST.get('card_valid_date')
        card_tran_amount = request.POST.get('amount')
        numbers = []
        card_level = 1
        if int(card_tran_amount) >= 20 and int(card_tran_amount) < 100:
            card_level = 2
        elif int(card_tran_amount) >= 100:
            card_level = 3

        for i in range(int(count)):
            number = random_with_N_digits(15)
            numbers.append('4' + str(number))

        for i in range(int(count)):
            card = Card(
                card_number=numbers[i],
                card_valid_date=card_valid_date,
                card_transaction_amount=card_tran_amount,
                card_level_membership=card_level
            )
            card.save()
            send_message('card_generated', {'id': card.id})
        return redirect('get_all_cards')
    return render(request, 'gen_card.html', context)

def get_card(request, card_id):
    form = Get_Cards()
    card = get_object_or_404(Card, pk=card_id)
    context = {'card': card,
               'form': form}
    return render(request, 'card.html', context=context)


def change_status_card(request, card_id):
    form = Get_Cards()
    card = get_object_or_404(Card, pk=card_id)
    context = {'card': card,
               'form': form}
    if card.card_status:
        card = Card.objects.filter(pk=card_id).update(card_status=False)
        return render(request, 'card.html', context=context)
    else:
        card = Card.objects.filter(pk=card_id).update(card_status=True)
        return render(request, 'card.html', context=context)


def update_card_tran(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    form = Get_Cards()
    context = {'card': card,
               'form': form}
    if request.method == 'POST':
        print(request.POST.get('amount'),'sh')

        if request.POST.get('amount') == '':# if nothing is input but user click the button, it will automatically switch to this page
            return render(request, 'card.html', context=context)

        new_amount = request.POST.get('amount')

        card_level = 1
        if int(new_amount) >= 20 and int(new_amount) < 100:
            card_level = 2
        elif int(new_amount) >= 100:
            card_level = 3
        card.card_transaction_amount = int(new_amount)
        card.card_level_membership = int(card_level)

        card.save()

    return render(request, 'card.html', context=context)



def delete_card(request, card_id):
    card = Card.objects.get(pk = card_id)
    card.delete()
    return redirect('get_all_cards')

    # try:
    # except Exception as e:




