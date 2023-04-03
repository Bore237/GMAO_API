from django.contrib.auth.models import User, Group
from models import Person, Societe,\
                   Machine, Stock, Operation
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = ['nom', 'prenom', 'email', 'phone', 'gps_pos','activite',
                'contrat', 'imatriculation','siège_social', 'type_societe']

class SocieteSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Societe
        fields = ['nom', 'email', 'phone', 'gps_pos']

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['nom', '', '', '', '']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['nom', '', '', '', '']

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['nom', '', '', '', '']