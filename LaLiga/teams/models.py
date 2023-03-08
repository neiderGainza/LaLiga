from django.db import models
from players import models as players_models

class Team(models.Model):
    name = models.CharField(primary_key=True, max_length = 200)

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


class Base(models.Model):
    action_name = " nothing "
    

    player = models.ForeignKey( players_models.Players, on_delete = models.CASCADE)
    game   = models.ForeignKey( Game, on_delete = models.CASCADE)
    time   = models.TimeField()

    def __str__(self):
        #consulta sobre nombre del jugador
        name = str( self.player )
        game = str( self.game ) 

        return self.action_name + " " + name + " " + game

class Goal(Base):
    action_name = "Gol"

class Yelow_Card(Base):
    action_name = "Tarjeta Amarilla"

class Red_Car(models.Model):
    action_name = "Tarjeta Roja"



class Assistance(models.Model):
    pass

class Change(models.Model):
    pass






