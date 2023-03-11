from django.db import models

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()

    teams      = models.ManyToManyField('teams.Team', through="Suscription")
    schedule_reference  = models.ManyToManyField("teams.Game", through="Schedule")    


class Suscription(models.Model):
    tournaments = models.ForeignKey("tournaments.Tournament", on_delete= models.CASCADE)
    teams       = models.ForeignKey("teams.Team",  on_delete= models.CASCADE)


class Schedule(models.Model):
    """
        esta relacion se encarga de guardar el grupo de partidos que forman
        parte de un torneo

        How will i representate this
    """
    tournament_name  = models.ForeignKey("Tournament", on_delete = models.CASCADE)
    game_name        = models.ForeignKey("teams.Game", on_delete = models.CASCADE)

