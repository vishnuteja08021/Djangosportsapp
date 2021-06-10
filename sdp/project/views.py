from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import  User
from django.contrib import auth,messages
from django.contrib.auth import authenticate

from .models import Feedback, NormalPay, PaymentForm,profile,profileForm
import numpy as np
import matplotlib.pyplot as plt
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def Profilepage(request):
    pform = profileForm(data=request.POST, instance=request.user)
    if request.method == "POST":
        pform = profileForm(request.POST)
        print(pform.is_valid())
        if pform.is_valid():
            # print("hello")
            pform.save()
            update = pform.save(commit=False)
            update.user = request.user
            update.save()
        else:
           form = profileForm(instance=request.user)
    return render(request,'profile.html',{'form':pform})
def contact(request):
    if request.method == "POST":
        print(request.POST['firstname'],request.POST['country'])
        f=Feedback(firstname=request.POST['firstname'],lastname=request.POST['lastname'],country=request.POST['country'],subject=request.POST['subject'])
        f.save()
        return render(request,'contact.html',{'success':'Feedback has been sent'})
    return render(request,'contact.html')
def login(request):
    try:
        print(request.POST['uname'],request.POST['upass'])
        u=User.objects.get(username=request.POST['uname'],password=request.POST['upass'])
        print(u)
        request.session['username']=request.POST['uname']
        if u is not None:
            return render(request,'home.html',{'name':request.POST['uname']})
    except:
        return render(request,'login.html')
    return render(request,'login.html')
def signup(request):

    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')
def games(request):
    return render(request,'games.html')
def news(request):
    return render(request,'news.html')
def Account(request):
    return render(request,'Account.html')
def logout(request):
    auth.logout(request)
    return render(request,'login.html')


def registeruser(request):
    if request.method == 'POST':

        if request.POST['upass'] == request.POST['urpass']:
            u = User(username = request.POST['uname'],email = request.POST['uemail'],password = request.POST['upass'])
            u.save()
            send_mail('The excitement that a gambler feels when making a bet is equal to the amount he might win times the probability of winning it.','welcome to play_clues ... !!!! the world of gambling awaits your arrival place the bets and earn the prfits play more and earn more','vishnuteja0802@gmail.com',[ request.POST['uemail']])
            HttpResponse('success')
        return redirect('login')

def Paymentpage(request):
    pform=PaymentForm()
    if request.method=="POST":
        pform=PaymentForm(request.POST)
        pform.save()
        ppform=PaymentForm()
        return render(request,'payment1.html',{'form':ppform,'success':'Your Payment has done successfully!'})
    return render(request,'payment1.html',{'form':pform})

def graphs(request):
    barWidth = 0.2
    fig = plt.subplots(figsize=(26, 11))
    IT = [27, 20, 6, 27, 12, 29, 11, 22, 37, 18, 24, 26]
    ECE = [16, 15, 13, 13, 13, 13, 13, 12, 12, 11, 11, 11]
    fifity = [4, 2, 1, 0, 1, 4, 1, 1, 3, 1, 2, 1]
    innings = [7, 7, 5, 7, 7, 7, 7, 6, 8, 7, 7]

    br1 = np.arange(len(IT))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]

    # Make the plot
    plt.bar(br1, IT, color='r', width=barWidth, edgecolor='grey', label='four')
    plt.bar(br2, ECE, color='b', width=barWidth, edgecolor='grey', label='sixes')
    plt.bar(br3, fifity, color='y', width=barWidth, edgecolor='grey', label='fifity')
    # Adding Xticks
    plt.xlabel('Branch', fontweight='bold', fontsize=8)
    plt.ylabel('sixes and foures and fifty', fontweight='bold', fontsize=8)
    plt.xticks([r + barWidth for r in range(len(IT))],
               ['kl rahul', 'johny bairstow', 'ambati rayudu', 'jos buttler', 'andre russell', 'faf du plessis',
                'kieron pollard', 'moeen ali', 'prithvi shaw', 'rohith sharma', 'mayank agrawal', 'sanju samson'])

    plt.legend()
    plt.savefig("media/plot.png")
    plt.clf()
    day = ['p1', 'p2', 'p3 ', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11']
    innings = [7, 7, 5, 7, 7, 7, 7, 6, 8, 7, 7]
    noouts = [2, 1, 1, 0, 1, 2, 4, 0, 0, 0, 1]
    line_chart1 = plt.plot(day, innings, color='Blue')
    line_chart2 = plt.plot(day, noouts, color='Red')
    plt.xlabel('players', color="green")
    plt.ylabel('innings and no outs', color="green")
    plt.title('Ipl 2021')
    plt.savefig("media/plot2.png")
    plt.clf()

    runs = [331, 248, 136, 254, 163, 320, 168, 206, 308, 250, 260, 277, 207, 223, 195, 201, 193, 93, 123, 116]
    plt.hist(runs, bins=[1, 101, 201, 301, 401])
    plt.xlabel('RUNS OF EACH PLAYER', color="red")
    plt.savefig("media/plot3.png")
    plt.clf()

    # creating the dataset
    data = {'CSK': 62, 'PBKS': 57, 'RR': 52,
            'KKR': 48, 'MI': 43, 'RCB': 43, 'SRH': 43, 'DC': 32}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(courses, values, color='maroon',
            width=0.4)

    plt.xlabel("TEAMS")
    plt.ylabel("No. OF SIXES")
    plt.savefig("media/plot4.png")
    plt.clf()
    barWidth = 0.2
    fig = plt.subplots(figsize=(26, 11))
    IT = [15, 14, 13, 12, 13, 11, 9, 8, 7, 7, 6, 4]
    ECE = [4, 5, 7, 8, 8, 10, 11, 13, 13, 12, 13, 15]

    br1 = np.arange(len(IT))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]

    # Make the plot
    plt.bar(br1, IT, color='r', width=barWidth, edgecolor='grey', label='')
    plt.bar(br2, ECE, color='b', width=barWidth, edgecolor='grey', label='')

    # Adding Xticks
    plt.xlabel('team names', fontweight='bold', fontsize=8)
    plt.ylabel('winning matches and losing matches in total 22 matches', fontweight='bold', fontsize=8)
    plt.xticks([r + barWidth for r in range(len(IT))],
               ['Dabang Delhi K.C.', 'Bengal Warriors', 'U.P. Yoddha', 'U Mumba', 'Haryana Steelers', 'Bengaluru Bulls',
                'Jaipur Pink Panthers', 'Patna Pirates', 'Gujarat Fortunegiants', 'Puneri Paltan', 'Telugu Titans',
                'Tamil Thalaivas'])

    plt.legend()
    plt.savefig("media/plotk1.png")
    plt.clf()

    x = [24, 24, 24, 23, 24, 22, 23, 22, 22, 22]
    y = [890, 868, 868, 809, 785, 774, 770, 744, 725, 700]

    plt.scatter(x, y, label='skitscat', color='k', s=30, marker="*")

    plt.xlabel('matches played')
    plt.ylabel('points')

    plt.title('kabadi team wise matches played \ntotal points')
    plt.legend()
    plt.savefig("media/plotk2.png")
    plt.clf()

    data = {'Name': ['pawankumar sehrawat', 'pradeep Narwal', 'Naveen kumar',
                     'Siddharth sirath', 'manider singh', 'vikash kandola', 'Abishek singh', 'Deepak niwas',
                     'shrikant jadhav', 'manjeet'],
            'Age': [24, 22, 23, 22, 20, 20, 21, 20, 22, 22]}

    # Load data into DataFrame
    import pandas as pd
    df = pd.DataFrame(data=data);
    x = df['Name']
    y = df['Age']
    plt.scatter(x, y)
    plt.xticks(rotation=90)
    plt.savefig("media/plotk3.png")
    return render(request,"graphs.html")