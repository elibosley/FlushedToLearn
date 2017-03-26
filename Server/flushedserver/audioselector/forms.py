from django import forms
from audioselector.models import MusicFile

class MediaForm(forms.ModelForm):
    class Meta:
        model = MusicFile
        fields = ('media',)
