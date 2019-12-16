from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Rafael'

doc = """
Encuesta demográfica
"""

class Constants(BaseConstants):
    name_in_url = 'app_7_question'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    gender = models.IntegerField(
        label = 'Geschlecht: ',
        choices = [(0, "Frauen"),
                   (1, "Männer"),
                   (2,"Andere")],
        widget = widgets.RadioSelectHorizontal
    )

    age = models.IntegerField(
        label = 'Alter: ',
        min = 18, max = 70
    )

    country = models.StringField(
        label = "Aus welchem Land stammen Sie?",
    )

    education = models.IntegerField(
        label = 'Welchen Bildungsgrad haben Sie (höchster erreichter Abschluss)?',
        choices = [(1, "Keine Schulbildung"),
                   (2, "Grund- und Hauptschule"),
                   (3, "Berufs(-fach-)schule / -ausbildung"),
                   (4, "Oberstufe (Abitur)"),
                   (5, "Universitärer Abschluss (Bachelor)"),
                   (6, "Höheres Studium (Master / Dr.)")]
    )

    civil_status = models.IntegerField(
        label = 'Was ist Ihr Personenstand?',
        choices = [(1, 'Single (nie verheiratet)'),
                   (2, 'Mit Partner/in zusammenlebend'),
                   (3, 'Verheiratet'),
                   (4, 'Getrennt / geschieden'),
                   (5, 'Verwitwet')]
    )

    income = models.IntegerField(
        label= 'Nur zu statistischen Klassifikationszwecken: Was ist das Bruttojahreseinkommen in Ihrem Haushalt gemäß den folgenden Kategorien?',
        choices = [
            (1, '0 - 20.000 Euro'),
            (2,'20.001 - 40.000 Euro'),
            (3,'40.001 - 60.000 Euro'),
            (4,'60.001 - 80.000 Euro'),
            (5,'80.001 - 100.000 Euro'),
            (6,'Über 100.000 Euro')])

    online_frequency = models.IntegerField(
        label = 'Wie häufig gehen Sie allgemein ins Internet?',
        choices = [
            (1, 'Durchgängig / jede Stunde'),
            (2, 'Mehrmals pro Tag'),
            (3, 'Einmal pro Tag'),
            (4, 'Mehrmals pro Woche'),
            (5, 'Einmal pro Woche'),
            (6, 'Seltener als einmal pro Woche')
        ]
    )

