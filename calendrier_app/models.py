from django.db import models

 

class Presence(models.Model):
    date = models.DateField()
    heure_arrive = models.TimeField(null=True,blank=True)
    heure_depart = models.TimeField(null=True,blank=True)
    noms = models.CharField(max_length=100)
    user_id = models.IntegerField()

    def __str__(self):
        return f"{self.noms} - {self.date}"
