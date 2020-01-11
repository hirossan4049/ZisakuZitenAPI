from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, filters, status, exceptions
from rest_framework.response import Response

from .models import Ziten,Group
from .serializer import ZitenSerializer,GroupSerializer
from rest_framework import generics
# Create your views here.


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    def perform_destroy(self, conversation):
        print("destoroooooooooy")
        if self.request.user.is_staff:
            conversation.delete()
            print("STAFF DELETE")
        else:
            print("NO STAFF DELETE")
            # return Response({'status': 'conversation has messages'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
            print("update!")
        else:
            print("NO STAFF cant update.")
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ZitenViewSet(viewsets.ModelViewSet):
    queryset = Ziten.objects.all()
    serializer_class = ZitenSerializer

    def perform_destroy(self, conversation):
        print("destoroooooooooy")
        if self.request.user.is_staff:
            conversation.delete()
            print("STAFF DELETE")
        else:
            print("NO STAFF DELETE")
            # return Response({'status': 'conversation has messages'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
            print("update!")
        else:
            print("NO STAFF cant update.")
            return Response(status=status.HTTP_400_BAD_REQUEST)


"""
class GroupDestroy(generics.DestroyAPIView):
    queryset =  Group.objects.all()
    serializer_class = GroupSerializer

    def perform_destroy(self, conversition):
        if conversition.message.exists():
            return Response({'status': 'conversation has messages'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            conversition.delete()
"""