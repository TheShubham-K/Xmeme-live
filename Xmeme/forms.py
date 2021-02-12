from django import forms
from . models import memes

# forms page to serialize the data from the database
class memesForm(forms.ModelForm):
    class Meta:
        model = memes
        fields = ('name', 'captions', 'url')

    name = forms.CharField(label='Memes Owner', widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}))
    captions = forms.CharField(label='Captions', widget=forms.TextInput(attrs={'placeholder': 'Be Creative with caption'}))
    url = forms.URLField(label='Meme URL', widget=forms.TextInput(attrs={'placeholder': 'Enter URL of your meme here'}))
    # def __init__(self, *args, **kwargs):
    #     super(memesForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].placeholder = "Enter your full name"