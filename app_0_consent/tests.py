from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random, itertools


class PlayerBot(Bot):
    names = itertools.cycle(['Alberto', 'Bolivar', 'Carlos', 'Danilo', 'Élmer', 'Facundo', 'Guillñrmo', 'Hernán', 'Idi8o', 'Janice', 'Kim/erly', 'Lola'])
    ids = itertools.cycle(['987A78A', '98A438A', '9B7878A', '9Cv78A', '934A78A', '987á78A', '989ó8A', '98´kA78A' '987-78A' '98*A78A' '987A78A'])
    def play_round(self):
        yield (pages.Bienvenido)
        yield (pages.Consent, {'nombre': next(self.names), 'id_number': next(self.ids)})

