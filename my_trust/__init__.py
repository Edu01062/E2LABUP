from otree.api import *
import random

doc = """
E2LABUP TRABAJO APP
"""



class C(BaseConstants):
    NAME_IN_URL = 'my_trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT=cu(10)
    M_FACTOR=3

class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    pass
    

#FUNCTIONS


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        label="Si fueras el jugador A, ¿cuánto enviarías de vuelta al Jugador B?",
        choices=list(range(int(C.ENDOWMENT) + 1))
    )
    sent_back_amount_case_1 = models.CurrencyField(
        label="Si fueras el jugador B y recibieras 3 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
        choices=list(range( 10))
    )
    sent_back_amount_case_2 = models.CurrencyField(
        label="Si fueras el jugador B y recibieras 6 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
        choices=list(range(19))
    )
    sent_back_amount_case_3 = models.CurrencyField(
        label="Si fueras el jugador B y recibieras 9 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
        choices=list(range(28))
    )
    def set_payoffs(self):
        A = self.get_player_by_id(1)
        B = self.get_player_by_id(2)
        if A.sent_amount <= 3:
            A.payoff = C.ENDOWMENT - A.sent_amount + B.sent_back_amount_case_1
            B.payoff = 3 * A.sent_amount - B.sent_back_amount_case_1
        elif A.sent_amount <= 6:
            A.payoff = C.ENDOWMENT - A.sent_amount + B.sent_back_amount_case_2
            B.payoff = 3 * A.sent_amount - B.sent_back_amount_case_2
        else:
            A.payoff = C.ENDOWMENT - A.sent_amount + B.sent_back_amount_case_3
            B.payoff = 3 * A.sent_amount - B.sent_back_amount_case_3



# PAGES

class Introduction(Page):
    pass


class Send(Page):
    form_model="group"
    form_fields=["sent_amount","sent_back_amount_case_1","sent_back_amount_case_2","sent_back_amount_case_3"]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    after_all_players_arrive = 'set_payoffs'

    

page_sequence = [Introduction,Send, ResultsWaitPage,Results]
