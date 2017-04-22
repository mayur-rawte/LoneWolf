from rest_framework import serializers,viewsets
from django.contrib.auth.models import User
from storybeta.models import Story, UserExtras, Iterations, Comments


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','is_staff')


class UserExtrasSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    class Meta:
        model = UserExtras
        fields = ('user_id','gaccount','faccount','phone','image')

class StorySerializer(serializers.ModelSerializer):
    main_author = UserSerializer()
    class Meta:
        model = Story
        fields = ('title','description','imageURL','passages','main_author','co_authors')



class IterationSerializer(serializers.ModelSerializer):
    story_id = StorySerializer()
    it_author = UserSerializer()
    class Meta:
        model = Iterations
        fields = ('story_id','it_author','liked_by','content')


class CommentSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    iteration_id = IterationSerializer()
    class Meta:
        model = Comments
        fields = ('user_id','iteration_id','content')

