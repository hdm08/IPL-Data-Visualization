from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Delivery,Matches

@admin.register(Matches)
class MatchesAdmin(ImportExportModelAdmin):
    list_display = ['id','season','city','date','team1','team2','toss_winner','toss_decision','result','dl_applied','winner','win_by_runs','win_by_wickets','player_of_match','venue','umpire1','umpire2','umpire3']
    list_filter = ('season', 'city','winner')
    search_fields = ('season', 'city','team1','team2','winner')
    ordering = ('id',)

@admin.register(Delivery)
class DeliveryAdmin(ImportExportModelAdmin):
    list_display = ['match_id',	'inning','batting_team','bowling_team','over','ball','batsman','non_striker','bowler','is_super_over','wide_runs','bye_runs','legbye_runs','noball_runs','penalty_runs','batsman_runs','extra_runs','total_runs','player_dismissed','dismissal_kind','fielder']
    list_filter = ('match_id', 'batting_team', 'bowling_team')
    search_fields = ('match_id', 'batting_team', 'bowling_team', 'batsman','bowler')
    ordering = ('match_id',)
