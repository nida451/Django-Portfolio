from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Profile, ChatRoom, Message
from .forms import ProfileForm, ChatRoomForm, MessageForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'chat/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors) 
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.profile.is_profile_complete:
                return redirect('profile_view')  
            else:
                return redirect('chat/add_profile_data.html')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

@login_required
def add_profile_data(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_profile_complete = True
            profile.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'chat/add_profile_data.html', {'form': form})

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    chat_rooms = ChatRoom.objects.filter(members=request.user)
    
    context = {
        'profile': profile,
        'chat_rooms': chat_rooms
    }
    
    return render(request, 'chat/profile.html', context)
#    return render(request, 'chat/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'chat/profile_edit.html', {'form': form})

@login_required
def create_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.save()
            chat_room.members.add(request.user)
            return redirect('chat_room', chat_room_id=chat_room.id)
    else:
        form = ChatRoomForm()
    return render(request, 'chat/create_chat_room.html', {'form': form})

@login_required
def chat_room(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
    messages = chat_room.messages.all()
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.user = request.user
            message.chat_room = chat_room
            message.save()
            return redirect('chat_room', chat_room_id=chat_room.id)
    else:
        message_form = MessageForm()
    return render(request, 'chat/chat_room.html', {
        'chat_room': chat_room,
        'messages': messages,
        'message_form': message_form,
    })

def chat_room_detail(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
    context = {
        'chat_room': chat_room
    }
    return render(request, 'chat/chat_room_detail.html', context)

def chat_room_list(request):
    # Retrieve all chat rooms
    chat_rooms = ChatRoom.objects.all()
    context = {
        'chat_rooms': chat_rooms
    }
    return render(request, 'chat/chat_room_list.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
