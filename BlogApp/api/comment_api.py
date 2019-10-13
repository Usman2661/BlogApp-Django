from rest_framework import serializers
from feed.models import Feeds
from comment.models import Comments
from rest_framework import viewsets

class CommentSerialiser(serializers.HyperlinkedModelSerializer):
    #UserID_id = UserIDSerializer(read_only=False)

    class Meta:

        model = Comments
        fields = ('id','PostID', 'UserID_id','Comment', 'DateTime')
    
class CommentViewSet(viewsets.ModelViewSet):
    
    queryset = Comments.objects.all()
    serializer_class = CommentSerialiser
