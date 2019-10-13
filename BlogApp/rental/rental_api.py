from rest_framework import serializers
from rental.models import Friend,Belonging,Borrowed
from rest_framework import viewsets


class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'name')

class BelongingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Belonging
        fields = ('id', 'name')

class BorrowedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')
    

class FriendViewSet(viewsets.ModelViewSet): 

    model = Friend    
    serializer_class = FriendSerializer

    def get_queryset(self):

        name = self.request.query_params.get('name')
        queryset = Friend.objects.filter(name=name)
        
        return queryset

class BelongingViewSet(viewsets.ModelViewSet):

    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer

class BowrrowedViewSet(viewsets.ModelViewSet):

    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer
