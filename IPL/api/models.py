from django.db import models

#_______________________________________________________________________________________________________________________

class Matches(models.Model):
    season=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    date=models.DateField()
    team1=models.CharField(max_length=100,default="")
    team2=models.CharField(max_length=100,default="")
    toss_winner=models.CharField(max_length=100,default="")
    toss_decision=models.CharField(max_length=100,default="")
    result=models.CharField(max_length=100,default="")
    dl_applied=models.IntegerField()
    winner=models.CharField(max_length=100,default="")
    win_by_runs=models.IntegerField()
    win_by_wickets=models.IntegerField()
    player_of_match=models.CharField(max_length=100,default="")
    venue=models.CharField(max_length=100,default="")
    umpire1=models.CharField(max_length=100,default="")
    umpire2=models.CharField(max_length=100,default="")
    umpire3=models.CharField(max_length=100,default="")

    def __str__(self):
        return str(self.id)

#_______________________________________________________________________________________________________________________

class Delivery(models.Model):
    match_id=models.ForeignKey(Matches,on_delete=models.CASCADE)
    inning=models.IntegerField()
    batting_team=models.CharField(max_length=100,default="")
    bowling_team=models.CharField(max_length=100,default="")
    over=models.IntegerField()
    ball=models.IntegerField()
    batsman=models.CharField(max_length=100,default="")
    non_striker=models.CharField(max_length=100,default="")
    bowler=models.CharField(max_length=100,default="")
    is_super_over=models.IntegerField()
    wide_runs=models.IntegerField()
    bye_runs=models.IntegerField()
    legbye_runs=models.IntegerField()
    noball_runs=models.IntegerField()
    penalty_runs=models.IntegerField()
    batsman_runs=models.IntegerField()
    extra_runs=models.IntegerField()
    total_runs=models.IntegerField()
    player_dismissed=models.CharField(max_length=100,default="")
    dismissal_kind=models.CharField(max_length=100,default="")
    fielder=models.CharField(max_length=100,default="")
    def __str__(self):
        return str(self.match_id)

#_______________________________________________________________________________________________________________________
