from rest_framework import serializers
from .models import Ziten,Group



class ZitenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ziten
        fields = ('title','content','updateTime','group')



class GroupSerializer(serializers.ModelSerializer):
    ziten_updT_List = ZitenSerializer(many=True,read_only=True)
    class Meta:
        model = Group
        fields = ('title','updateTime','id','ziten_updT_List')
