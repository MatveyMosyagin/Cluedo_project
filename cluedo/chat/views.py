from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
import random
from django.core.mail import EmailMessage

room_cards = ['ballroom', 'billiardroom', 'canteen', 'garden', 'hall', 'kitchen', 'library', 'livingroom', 'office']
weapon_cards = ['candlestick', 'dagger', 'lead pipe', 'revolver', 'rope', 'wrench']
people_cards = ['Green', 'Mustard', 'Orchid', 'Scarlett', 'Peacock', 'Plum']
random_rooms = []
random_weapons = []
random_people = []
users_email = []
users_names = []
count_of_lobbies = []
a = '.jpg'
b = 0


# Create your views here.
def main(request):
    return render(request, 'main.html')


def howtoplay(request):
    return render(request, 'Howtoplay.html')


def support(request):
    return render(request, 'support.html')


def success(request):
    return render(request, 'success.html')


def rules(request):
    return render(request, 'Rules.html')


def home(request):
    return render(request, 'Home.html')



def room(request, room):
    username = request.GET.get('username')
    email = request.GET.get('email')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'email': email,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    email = request.POST['email']
    users_email.append(email)
    users_names.append(username)
    print(users_names)
    print(users_email)

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    if len(count_of_lobbies) == 0:
        new_room = Room.objects.create(name=room)
        count_of_lobbies.append(room)
        print(room)
        print(count_of_lobbies)
        new_room.save()
        random_rooms.append(random.sample(room_cards, len(room_cards)))
        random_weapons.append(random.sample(weapon_cards, len(weapon_cards)))
        random_people.append(random.sample(people_cards, len(people_cards)))
        print(random_rooms, random_people, random_weapons)
        return redirect('/' + room + '/?username=' + username)
    else:
        users_email.pop()
        users_names.pop()
        count_of_lobbies.pop()
        print(count_of_lobbies)
        print(users_names)
        print(users_email)
        return render(request, 'Error.html')

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    if message == 'start':
        if len(users_email) == 3:
            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[0]])
            mail.attach_file(random_people[0][1] + a)
            mail.attach_file(random_weapons[0][1] + a)
            mail.attach_file(random_rooms[0][1] + a)
            mail.attach_file(random_weapons[0][4] + a)
            mail.attach_file(random_rooms[0][4] + a)
            mail.attach_file(random_rooms[0][6] + a)
            mail.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail2 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[1]])
            mail2.attach_file(random_people[0][2] + a)
            mail2.attach_file(random_weapons[0][2] + a)
            mail2.attach_file(random_rooms[0][2] + a)
            mail2.attach_file(random_weapons[0][5] + a)
            mail2.attach_file(random_people[0][5] + a)
            mail2.attach_file(random_rooms[0][7] + a)
            mail2.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail3 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[2]])
            mail3.attach_file(random_people[0][3] + a)
            mail3.attach_file(random_weapons[0][3] + a)
            mail3.attach_file(random_rooms[0][3] + a)
            mail3.attach_file(random_people[0][4] + a)
            mail3.attach_file(random_rooms[0][5] + a)
            mail3.attach_file(random_rooms[0][8] + a)
            mail3.send()
        if len(users_email) == 4:
            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[0]])
            mail.attach_file(random_people[0][1] + a)
            mail.attach_file(random_weapons[0][1] + a)
            mail.attach_file(random_rooms[0][1] + a)
            mail.attach_file(random_weapons[0][5] + a)
            mail.attach_file(random_rooms[0][5] + a)
            mail.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail2 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[1]])
            mail2.attach_file(random_people[0][2] + a)
            mail2.attach_file(random_weapons[0][2] + a)
            mail2.attach_file(random_rooms[0][2] + a)
            mail2.attach_file(random_people[0][5] + a)
            mail2.attach_file(random_rooms[0][6] + a)
            mail2.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail3 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[2]])
            mail3.attach_file(random_people[0][3] + a)
            mail3.attach_file(random_weapons[0][3] + a)
            mail3.attach_file(random_rooms[0][3] + a)
            mail3.attach_file(random_rooms[0][7] + a)
            mail3.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail4 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[3]])
            mail4.attach_file(random_people[0][4] + a)
            mail4.attach_file(random_weapons[0][4] + a)
            mail4.attach_file(random_rooms[0][4] + a)
            mail4.attach_file(random_rooms[0][8] + a)
            mail4.send()
        if len(users_email) == 5:
            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[0]])
            mail.attach_file(random_people[0][1] + a)
            mail.attach_file(random_weapons[0][1] + a)
            mail.attach_file(random_rooms[0][1] + a)
            mail.attach_file(random_rooms[0][6] + a)
            mail.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail2 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[1]])
            mail2.attach_file(random_people[0][2] + a)
            mail2.attach_file(random_weapons[0][2] + a)
            mail2.attach_file(random_rooms[0][2] + a)
            mail2.attach_file(random_rooms[0][7] + a)
            mail2.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail3 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[2]])
            mail3.attach_file(random_people[0][3] + a)
            mail3.attach_file(random_weapons[0][3] + a)
            mail3.attach_file(random_rooms[0][3] + a)
            mail3.attach_file(random_rooms[0][8] + a)
            mail3.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail4 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[3]])
            mail4.attach_file(random_people[0][4] + a)
            mail4.attach_file(random_weapons[0][4] + a)
            mail4.attach_file(random_rooms[0][4] + a)
            mail4.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail5 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[4]])
            mail5.attach_file(random_people[0][5] + a)
            mail5.attach_file(random_weapons[0][5] + a)
            mail5.attach_file(random_rooms[0][5] + a)
            mail5.send()
        if len(users_email) == 6:
            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[0]])
            mail.attach_file(random_people[0][1] + a)
            mail.attach_file(random_weapons[0][1] + a)
            mail.attach_file(random_rooms[0][1] + a)
            mail.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail2 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[1]])
            mail2.attach_file(random_people[0][2] + a)
            mail2.attach_file(random_weapons[0][2] + a)
            mail2.attach_file(random_rooms[0][2] + a)
            mail2.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail3 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[2]])
            mail3.attach_file(random_people[0][3] + a)
            mail3.attach_file(random_weapons[0][3] + a)
            mail3.attach_file(random_rooms[0][3] + a)
            mail3.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail4 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[3]])
            mail4.attach_file(random_rooms[0][6] + a)
            mail4.attach_file(random_weapons[0][4] + a)
            mail4.attach_file(random_rooms[0][4] + a)
            mail4.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail5 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[4]])
            mail5.attach_file(random_people[0][5] + a)
            mail5.attach_file(random_rooms[0][7] + a)
            mail5.attach_file(random_rooms[0][5] + a)
            mail5.send()

            subject = 'Hello Player, There is your cards! Have a good game!'
            text = "Please, don't show your cards to anyone"
            mail6 = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[5]])
            mail6.attach_file(random_people[0][4] + a)
            mail6.attach_file(random_weapons[0][5] + a)
            mail6.attach_file(random_rooms[0][8] + a)
            mail6.send()
    if message == 'assumption':
        subject = 'Hello Player, You make an assumption!'
        text = "Please, don't show this cards to anyone"
        index = users_names.index(username)
        mailx = EmailMessage(subject, text, 'mosmat1303@gmail.com', [users_email[index]])
        mailx.attach_file(random_people[0][0] + a)
        mailx.attach_file(random_weapons[0][0] + a)
        mailx.attach_file(random_rooms[0][0] + a)
        mailx.send()
    if message == 'finish':
        print(count_of_lobbies)
        count_of_lobbies.clear()
        users_email.clear()
        users_names.clear()
        random_rooms.clear()
        random_weapons.clear()
        random_people.clear()
        print(users_email)
        print(users_names)
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
