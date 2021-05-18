#pip install msvc-runtime

from django.shortcuts import render
from django.http import HttpResponse
from .resources import DeliveryResource
from tablib import Dataset
from .models import Delivery,Matches
from django.db.models import Count,Sum
from .utils import get_bar_year,get_stack_bar,get_multi_chart,get_extra_run,get_eco_bar

#_______________________________________________________________________________________________________________________

year = Matches.objects.values_list('season', flat=True).order_by('season').distinct()

#_______________________________________________________________________________________________________________________


def MatchePlayed(request):
    # print(year)
    no_of_mat=Matches.objects.values_list('season').annotate(Count('season'))
    # print(no_of_mat)
    mat_dict=dict(no_of_mat)
    # print(mat_dict)
    x=list(mat_dict.keys())
    y=list(mat_dict.values())
    # print(x,y)
    chart=get_bar_year(x,y)
    return render(request,'home.html',{'chart':chart,'year':year})

#_______________________________________________________________________________________________________________________


def Mat_Played(team1,team2):
    l = []
    for i in range(len(team1)):
        mat_list = list(team1[i] + team2[i])
        mat_list.pop(-2)
        x = mat_list.pop() + mat_list.pop()
        mat_list.append(x)
        l.append(tuple(mat_list))
    return l

def MatchStackBar(request):
    of_year=request.GET.get('graph','2008')

    team1=Matches.objects.values_list('team1').filter(season=of_year).order_by('team1').annotate(Count('season'))
    team2=Matches.objects.values_list('team2').filter(season=of_year).order_by('team2').annotate(Count('season'))
    mat_palyed_per_team=Mat_Played(team1,team2)
    # print(mat_palyed_per_team)

    total_mat_win_per_team = list(Matches.objects.values_list('winner').filter(season=of_year).order_by('winner').annotate(Count('season')))
    # print(total_mat_win_per_team)

    for k in total_mat_win_per_team:
        if k[0]=="":
            total_mat_win_per_team.remove(k)
    # print(total_mat_win_per_team)

    final_list=[]
    for j in range(len(mat_palyed_per_team)):
        final = list(mat_palyed_per_team[j] + total_mat_win_per_team[j])
        final.pop(-2)
        final_list.append(final)
    chart=get_stack_bar(final_list,of_year)

    return render(request, 'allchart.html', {'chart': chart,'year':year})

#_______________________________________________________________________________________________________________________


def ExtraRunConceded(request):
    of_year=request.GET.get('graph','2008')

    team1 = Matches.objects.values_list('team1',flat=True).filter(season=of_year).order_by('team1').distinct()
    # print(team1)
    match_ids = Matches.objects.values_list('id',flat=True).filter(season=of_year)
    # print(match_ids)

    teamlist=[]
    for team in team1:
        run = 0
        tup = []

        for matchid in match_ids:
            dele = Delivery.objects.values_list('bowling_team').filter(match_id=matchid,bowling_team=team).annotate(Sum('extra_runs'))
            for a,b in dele:
                run=run+b
        tup.append(team)
        tup.append(run)
        teamlist.append(tuple(tup))
    # print(teamlist)

    chart=get_extra_run(teamlist,of_year)

    return render(request,'allchart.html',{'chart':chart,'year':year})

#_______________________________________________________________________________________________________________________


def EconomicalBowler(request):
    of_year = request.GET.get('graph', '2008')

    match_ids = Matches.objects.values_list('id', flat=True).filter(season=of_year)

    bow=[]
    for matchid in match_ids:
        bowler = list(Delivery.objects.values_list('bowler', flat=True).filter(match_id=matchid).distinct())
        bow.extend(bowler)
    bowlist=list(set(bow))
    bowlist.sort()
    # print(bowlist)

    tuplist = []
    for bowl in bowlist:
        ball=0
        run=0
        tup=[]
        for matchid in match_ids:
            bowlrun = Delivery.objects.values_list('bowler').filter(match_id=matchid,bowler=bowl).annotate(Count('bowler'),Sum('total_runs'))
            for a,b,c in bowlrun:
                ball=ball+b
                run=run+c
        over=ball//6
        economy=round(run/over,2)
        tup.append(bowl)
        tup.append(economy)
        tuplist.append(tuple(tup))

    tuplist.sort(key=lambda x: x[1])
    finalist=tuplist[0:10]
    chart=get_eco_bar(finalist,of_year)

    return render(request,'allchart.html',{'chart':chart,'year':year})

#_______________________________________________________________________________________________________________________


def MatchesPlayedWon(request):
    of_year=request.GET.get('graph','2008')

    team1=Matches.objects.values_list('team1').filter(season=of_year).order_by('team1').annotate(Count('season'))
    team2=Matches.objects.values_list('team2').filter(season=of_year).order_by('team2').annotate(Count('season'))
    mat_palyed_per_team=Mat_Played(team1,team2)
    # print(mat_palyed_per_team)

    total_mat_win_per_team = list(Matches.objects.values_list('winner').filter(season=of_year).order_by('winner').annotate(Count('season')))
    # print(total_mat_win_per_team)

    for k in total_mat_win_per_team:
        if k[0]=="":
            total_mat_win_per_team.remove(k)
    # print(total_mat_win_per_team)

    final_list=[]
    for j in range(len(mat_palyed_per_team)):
        final = list(mat_palyed_per_team[j] + total_mat_win_per_team[j])
        final.pop(-2)
        final_list.append(final)
    # print(final_list)

    chart=get_multi_chart(final_list,of_year)

    return render(request, 'allchart.html', {'chart': chart,'year':year})

#_______________________________________________________________________________________________________________________

from .serializer import MatchesSerializer,DeliverySerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser

#_______________________________________________________________________________________________________________________

class MatchAPI(viewsets.ModelViewSet):
    queryset =Matches.objects.all()
    serializer_class = MatchesSerializer
    pagination_class = PageNumberPagination
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['=id','=season','city','team1','team2','city','venue']
    filterset_fields=['season']
    ordering_fields=['season','date']
    ordering = ['season']
    authentication_classes = [BasicAuthentication]
    permission_classes  = [IsAuthenticated]

#_______________________________________________________________________________________________________________________

class DeliveryAPI(viewsets.ModelViewSet):
    queryset =Delivery.objects.all()
    serializer_class = DeliverySerializer
    pagination_class = PageNumberPagination
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['=match_id','batsman','dismissal_kind']
    filterset_fields=['match_id','inning']
    ordering_fields=['match_id','date']
    ordering = ['match_id']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#_______________________________________________________________________________________________________________________













def simple_upload(request):
    if request.method == 'POST':
        person_resource = DeliveryResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read().decode(),format='csv')
        #print(imported_data)
        i=1
        for data in imported_data:
            print(data[2])
            value = Delivery(
                i,
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
                data[19],
                data[20],
            )
            value.save()
            i+=1
    return render(request, 'input.html')