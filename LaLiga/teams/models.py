from django.db import models
from players import models as players_models


class Team(models.Model):
    name = models.CharField(primary_key=True, max_length = 200)
    #picture = models.ImageField()

    capitan = models.ForeignKey(players_models.Players, on_delete=models.SET_NULL,null=True, blank=True)
    games = models.ManyToManyField(to = 'self', through="Game")

    def __str__(self):
        return self.name


class Game(models.Model):
    # Django no acepta que desde un modelo se tengan dos llaves foraneas al mismo modelo
    
    teams = models.ManyToManyField('Team')

    date  = models.DateField(auto_now=True)
    time  = models.TimeField(auto_now=True)

    def __str__(self):
        partido = ""
        
        for team in self.teams.all():
            partido += " vs "+ team.name + " " 
        
        return partido[4:]


class Base_Type_1:
    action_name = " nothing "
    bridge1 = " a "

    player = models.ForeignKey( players_models.Players, on_delete = models.CASCADE)
    game   = models.ForeignKey( Game, on_delete = models.CASCADE)
    time   = models.TimeField()

    def __str__(self):
        return self.action_name + bridge1 + self.player.name 



class Goal(models.Model, Base_Type_1):
    action_name = "Gol"
    bridge1 = " de "

class Yelow_Card(models.Model,Base_Type_1):
    action_name = "Tarjeta Amarilla"

class Red_Car(models.Model, Base_Type_1):
    action_name = "Tarjeta Roja"



class Assistance(models.Model, Base_Type_1):
    gol = models.ForeignKey(Goal, on_delete = models.CASCADE)

    def __str__(self):
        return "Asistencia de " + self.player.name + " para " + self.gol.player.name


class Change(models.Model):
    pass






