from rest_framework import serializers
from .models import Matches,Delivery

#_______________________________________________________________________________________________________________________

class MatchesSerializer(serializers.ModelSerializer):
    Edit=serializers.HyperlinkedIdentityField(view_name='match-detail')

    class Meta:
        model=Matches
        fields=['Edit','id','season','city','date','team1','team2','toss_winner','toss_decision','result','dl_applied','winner',
                'win_by_runs','win_by_wickets','player_of_match','venue','umpire1','umpire2','umpire3']
#_______________________________________________________________________________________________________________________

class DeliverySerializer(serializers.ModelSerializer):
    Edit=serializers.HyperlinkedIdentityField(view_name='delivery-detail')

    class Meta:
        model=Delivery
        fields = ['Edit','match_id', 'inning', 'batting_team', 'bowling_team', 'over', 'ball', 'batsman', 'non_striker',
                        'bowler', 'is_super_over', 'wide_runs', 'bye_runs', 'legbye_runs', 'noball_runs',
                        'penalty_runs', 'batsman_runs', 'extra_runs', 'total_runs', 'player_dismissed',
                        'dismissal_kind', 'fielder']
#_______________________________________________________________________________________________________________________