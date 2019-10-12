from rest_framework import serializers
from feed.models import Feeds
from rest_framework import viewsets

class NoteSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Feeds
        fields = ('PostTitle', 'PostMessage', 'Image', 'Catagory', 'DateTime','UserID_id')
    
class NoteViewSet(viewsets.ModelViewSet):
    
    queryset = Feeds.objects.all()
    serializer_class = NoteSerialiser

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = Feeds.objects.all().filter(UserID=7)
    serializer_class = NoteSerialiser