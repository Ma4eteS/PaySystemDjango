from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django_tables2 import SingleTableView

from .tables import PriceTable
from stripe_api.models import Item

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
domain_url = 'http://localhost:8000/'


class HomePageView(SingleTableView):
    model = Item
    table_class = PriceTable
    template_name = 'home.html'


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def buy(request, _id):
    if request.method == 'GET':
        try:
            item = Item.objects.get(pk=_id)
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    'price_data': {
                        'currency': "USD",
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': item.price*100,
                    },
                    'quantity': 1,
                }],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class ItemBuyView(TemplateView):
    template_name = 'item_buy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = Item.objects.get(pk=context["_id"])
        item_info = {
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "currency": "USD"
        }
        context.update(item_info)
        return context


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
