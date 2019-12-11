from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class instructions(Page):
    form_model = 'player'


class instructions_2(Page):
    pass


class MyWaitPage(WaitPage):
    def is_displayed(self):
        return self.player.role() == 'buyer'

    title_text = "You are a Buyer"
    body_text = "Please wait while the sellers set their offers"


class seller(Page):
    form_model = 'player'
    form_fields = ['ask_price_ini',
                   'see_list',
                   'com_practice'
                   ]

    def is_displayed(self):
        return self.player.role() != 'buyer'

    def vars_for_template(self):
        return dict(
            seller_package = self.player.seller_package,
            role = self.participant.vars['role']
        )

class SellerWaitPage(WaitPage):
    def is_displayed(self):
        return self.player.role() == 'seller'

    title_text = "Please Wait"
    body_text = "Please wait while the other sellers set their prices"

#TODO: Fix sellers IDs so they show from 1 to 10 instead of 1 to 19
class seller_2(Page):
    form_model = 'player'
    form_fields = [
        'ask_price_fin'
    ]
    def is_displayed(self):
        return self.player.role() != 'buyer'

    def vars_for_template(self):
        dict(
            role = self.player.role()
        )
#TODO: On the options list values should be shown with ECU con the side.
#TODO: Fix how Drip price is displayed in buyer ppage. If final price is 80, drip proce should show 78*.
class buyer(Page):
    timeout_seconds = 500
    form_model = 'player'
    form_fields = ['my_seller'] #la idea es que como tengo la id en group, puedo recuperar qué estaba vendiendo y a cómo.

    def is_displayed(self):
        return self.player.role() != 'seller'

    def vars_for_template(self):
        import time
        self.player.time_spent = time.time()
        return dict(
            role = self.participant.vars['role'],
            pac_val = self.participant.vars['valuations'],
            #parece que esto que sigue es innecesario
            #pac1 = self.player.buyer_valuation_pac1,
            #pac2 = self.player.buyer_valuation_pac2,
            #pac3 = self.player.buyer_valuation_pac3,
            #pac4 = self.player.buyer_valuation_pac4,
            #pac5 = self.player.buyer_valuation_pac5
        )

class ResultsWaitPage(WaitPage):
    pass

#TODO: Fix "You was too late..." for "It took you too long to make a decision. For this reason, your profit for this trading round are 0."
class Results(Page):
    def vars_for_template(self):
        self.group.set_payoff()
        self.group.who_purchased()

        return dict(
            role = self.participant.vars['role'],
            payoff = self.player.payoff,
            package = self.player.package_purchased,
            price = self.player.paid,
            seller = self.player.my_seller,
            sold = self.player.sold
        )



page_sequence = [instructions,
                 instructions_2,
                 seller,
                 SellerWaitPage,
                 seller_2,
                 MyWaitPage,
                 buyer,
                 ResultsWaitPage,
                 Results
                 ]


