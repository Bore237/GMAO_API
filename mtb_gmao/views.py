from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters

from mtb_gmao.models import Person, Societe, Stock, Machine, Operation
from mtb_gmao.serializers import UserSerializer, GroupSerializer,\
SocieteSerializer, PersonSerializer

"""
    All the view for admin project
"""
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


"""
    viewsset  of model 
"""
class SocieteViewSet(viewsets.ModelViewSet):
    """_summary_: Viewset of societe

    Args:
        viewsets (_type_): _description_
    """
    serializer_class = SocieteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'siege_social', 'type_societe']

    state_buton = False

    def get_queryset(self):
        queryset = Societe.objects.all().order_by('name')
        name = self.request.GET.get('name')

        if(self.state_buton == False):
            queryset = queryset.exclude(type_societe = 'None')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class PersonViewSet(viewsets.ModelViewSet):
    """_summary_: Viewset of person

    Args:
        viewsets (_type_): _description_
    """
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    detail_serializer_class = SocieteSerializer
    state_buton = False

    def get_queryset(self):
        queryset = Person.objects.all().order_by('name')
        name_company = self.request.GET.get('nom_societe__name')

        if(self.state_buton == False):
            queryset = queryset.exclude(type_contract = 'None')
        if name_company is not None:
            queryset = queryset.filter(name=name_company)
        return queryset
