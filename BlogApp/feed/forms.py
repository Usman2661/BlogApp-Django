from django import forms
from feed.models import Feeds

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feeds
        fields = ('PostTitle', 'PostMessage','Image','Catagory',)