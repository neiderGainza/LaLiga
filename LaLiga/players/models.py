from django.db import models
# Create your models here.


class Players(models.Model):
    id   = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    #picture = models.ImageField() 

    teams = models.ManyToManyField(to = 'teams.Team', through= 'Belong')
    
    registration_date = models.DateField(auto_now=True)
    birth_date        = models.DateField(auto_now=False,blank=True)


    def __str__(self):
        return self.name



class Belong(models.Model):
    player = models.ForeignKey(to = Players, on_delete = models.CASCADE)
    team   = models.ForeignKey(to = 'teams.Team', on_delete = models.CASCADE)
    
    since = models.DateField(auto_now=True)
    until = models.DateField(blank=True, default= "yet")

    def __str__(self):
        return self.player + " belongs to " + self.team + " since " + self.since + " until " + self.until