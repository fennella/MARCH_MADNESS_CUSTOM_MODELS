from django.db import models

# Create your models here.
class Team(models.Model):

    teamID = models.CharField(max_length=200, primary_key=True, default=None)
    name = models.CharField(max_length=200)
    lineNumber = models.IntegerField()
    SOS = models.FloatField(max_length=10, default=0)
    RPI = models.FloatField(max_length=10, default=0)
    PythW = models.FloatField(max_length=10, default=0)
    last10 = models.FloatField(max_length=10, default=0)
    top25 = models.FloatField(max_length=10, default=0)
    nonConf = models.FloatField(max_length=10, default=0)
    wp = models.FloatField(max_length=10, default=0)
    awp = models.FloatField(max_length=10, default=0)
    awayWP = models.FloatField(max_length=10, default=0)
    owp = models.FloatField(max_length=10, default=0)
    oowp = models.FloatField(max_length=10, default=0)
    pace = models.FloatField(max_length=10, default=0)
    ts = models.FloatField(max_length=10, default=0)
    efg = models.FloatField(max_length=10, default=0)
    ortg = models.FloatField(max_length=10, default=0)
    drtg = models.FloatField(max_length=10, default=0)
    nrtg = models.FloatField(max_length=10, default=0)
    ftr = models.FloatField(max_length=10, default=0)
    tovr = models.FloatField(max_length=10, default=0)
    dm = models.FloatField(max_length=10, default=0)
    orb = models.FloatField(max_length=10, default=0)
    erb = models.FloatField(max_length=10, default=0)
    blkp = models.FloatField(max_length=10, default=0)
    aps = models.FloatField(max_length=10, default=0)
    apa = models.FloatField(max_length=10, default=0)
    apd = models.FloatField(max_length=10, default=0)
    afbp = models.FloatField(max_length=10, default=0)
    ascp = models.FloatField(max_length=10, default=0)
    apip = models.FloatField(max_length=10, default=0)
    threepp = models.FloatField(max_length=10, default=0)
    ftp = models.FloatField(max_length=10, default=0)
    fgp = models.FloatField(max_length=10, default=0)
    aa = models.FloatField(max_length=10, default=0)
    avgs = models.FloatField(max_length=10, default=0)
    at = models.FloatField(max_length=10, default=0)
    ab = models.FloatField(max_length=10, default=0)
    aorb = models.FloatField(max_length=10, default=0)

    def __str__(self):
        return f'{self.name}'


    