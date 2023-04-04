from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
# from rest_framework import filters

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
    Filter models view of api 
"""
class SocieteFilter(filters.FilterSet):
    type_societe = filters.CharFilter(field_name='type_societe', lookup_expr='iexact')
    residence = filters.CharFilter(field_name='siege_social', lookup_expr='iexact')
    nom = filters.CharFilter(field_name="name", lookup_expr='iexact')

    class Meta:
        model = Societe
        fields = ['name', 'siege_social', 'type_societe']

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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SocieteFilter

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['nom', 'residence', 'type_societe']

    state_buton = False

    def get_queryset(self):
        queryset = Societe.objects.all().order_by('name')

        if(self.state_buton == False):
            queryset = queryset.exclude(type_societe = 'None')
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

        if(self.state_buton == False):
            queryset = queryset.exclude(type_contract = 'None')
        return queryset
