from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Freya Moßig wants to do her homework'
doc = 'Your app description goes here'


class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    counter = models.IntegerField(initial=0)
    # this is how you can implement variables that can be used by every player
    # they are called group variables and useful for example when quota checking


class Player(BasePlayer):
    # this is the most important feature of this file. We can collect all the variables used on the html pages here

    # The Variables are structured on the base of pages
    entry_question = models.IntegerField(choices=[[1, 'A lot'],
                                                  [2, 'I love cats!'],
                                                  [3, 'I cannot wait to start'],
                                                  ]
                                         )
    number_cats_question = models.IntegerField(blank=True, min=0)
    color = models.IntegerField(initial=-999)
    best_cat_name_question = models.StringField(blank=True)

    # custom error message
    # has to:
    # 1) be in the class Player (important to indent the right way)
    # 2) have a specific name "variablename"_error_message
    def number_cats_question_error_message(player, value):
        if not type(value) == int:
            return "Please enter an integer."
        if value < 0:
            return 'No one can pet less than 0 cats! In which mathematical world do you live?'
