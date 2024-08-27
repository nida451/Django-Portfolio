from django import forms
from .models import Profile, ChatRoom, Message

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']