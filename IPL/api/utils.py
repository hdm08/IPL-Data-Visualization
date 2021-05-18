from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()#it is byte value
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')#string decoded from base64 to utf-8
    buffer.close()
    return graph

#_______________________________________________________________________________________________________________________

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

def get_bar_year(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5),facecolor='silver')
    # ax = plt.axes()
    # ax.set_facecolor("gray")
    plt.title('Number of matches played per year')
    plot=plt.bar(x,y)
    print(plot)
    addlabels(x,y)

    # plt.xticks(rotation=45)
    plt.xlabel('year')
    plt.ylabel('No of Matches')
    plt.tight_layout()

    graph=get_graph()
    return graph

#_______________________________________________________________________________________________________________________

replacement = {
    'Chennai Super Kings': 'CSK',
    'Delhi Daredevils': 'DD',
    'Deccan Chargers': 'DC',
    'Gujarat Lions': 'GL',
    'Kings XI Punjab': 'KXIP',
    'Kolkata Knight Riders': 'KKR',
    'Mumbai Indians': 'MI',
    'Rising Pune Supergiants': 'RPS',
    'Rising Pune Supergiant': 'RPS',
    'Rajasthan Royals': 'RR',
    'Royal Challengers Bangalore': 'RCB',
    'Sunrisers Hyderabad': 'SRH',
    'Pune Warriors': 'PW',
    'Kochi Tuskers Kerala': 'KTK'
}

iplcolor = {
    'CSK':'yellow',
    'DD':'cornflowerblue',
    'DC':'navy',
    'GL':'orange',
    'KXIP':'maroon',
    'KKR':'purple',
    'MI':'blue',
    'RPS':'rebeccapurple',
    'RR':'hotpink',
    'RCB':'red',
    'SRH':'orangered',
    'PW':'black',
    'KTK':'coral'
}

#_______________________________________________________________________________________________________________________

def get_stack_bar(finalist,of_year):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5),facecolor='silver')
    ax = plt.axes()
    ax.set_facecolor("gray")
    x = []
    y1 = []
    y2 = []
    for team in finalist:
        x.append(team[0])
        y1.append(team[-1])
        y2.append(team[-2])
    print(x,y1,y2)

    x = [replacement.get(a, a) for a in x]

    bar1=plt.bar(x,y2,0.5,color='navy')
    bar2=plt.bar(x,y1,0.5,bottom=y2,color='yellow')
    plt.legend((bar1, bar2), ('Match Played', 'Match Won'))
    # plt.xticks(rotation=45)
    plt.title('Stack graph of '+of_year)
    plt.xlabel('Teams')
    plt.ylabel('No of Matches')
    plt.tight_layout()

    graph=get_graph()
    return graph

#_______________________________________________________________________________________________________________________

def get_extra_run(teamlist,of_year):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5),facecolor='silver')
    ax = plt.axes()
    ax.set_facecolor("whitesmoke")
    x = []
    y= []
    for team in teamlist:
        x.append(team[0])
        y.append(team[-1])

    x = [replacement.get(a, a) for a in x]

    plt.bar(x, y,0.6, color=[iplcolor.get(a, a) for a in x])
    addlabels(x, y)

    # plt.legend((bar1, bar2), ('Match Won', 'Match Played'))

    # plt.xticks(rotation=45)
    plt.title('Extra run conceded in '+of_year)
    plt.xlabel('Teams')
    plt.ylabel('Extra run conceded')
    plt.tight_layout()

    graph = get_graph()
    return graph

#_______________________________________________________________________________________________________________________


def get_eco_bar(finalist,of_year):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5),facecolor='silver')
    ax = plt.axes()
    ax.set_facecolor("gray")
    x = []
    y = []
    for bowler in finalist:
        x.append(bowler[0])
        y.append(bowler[-1])

    plt.bar(x,y,0.6,color='greenyellow')
    addlabels(x, y)
    # plt.xticks(rotation=45)
    plt.title('top 10 Economical bowler of '+ of_year)
    plt.xlabel('Bowler')
    plt.ylabel('Economy')
    plt.tight_layout()

    graph=get_graph()
    return graph

#_______________________________________________________________________________________________________________________


def label_multibar(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2, 1.0*height,
                 '%d' % int(height),
                 ha='center', va='bottom')

def get_multi_chart(finalist,of_year):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5),facecolor='silver')
    ax = plt.axes()
    ax.set_facecolor("gray")
    x = []
    y1 = []
    y2 = []
    for team in finalist:
        x.append(team[0])
        y1.append(team[-1])
        y2.append(team[-2])
    print(x,y1,y2)

    x = [replacement.get(a, a) for a in x]

    X_axis = np.arange(len(x))

    bar1=plt.bar(X_axis-0.2, y1, 0.4, label='match won',color='yellow')
    label_multibar(bar1)
    bar2= plt.bar(X_axis + 0.2, y2, 0.4, label='match played',color='b')
    label_multibar(bar2)

    plt.xticks(X_axis, x)
    plt.legend((bar1, bar2), ('Match Won', 'Match Played'))
    plt.title('No of matches played and won in '+of_year)
    plt.xlabel('Teams')
    plt.ylabel('No of Matches')
    plt.tight_layout()

    graph=get_graph()
    return graph
#_______________________________________________________________________________________________________________________
