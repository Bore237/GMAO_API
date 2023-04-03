from django.contrib.auth.models import User, Group
from models import Person, Societe,\
                   Machine, Stock, Operation
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields =  ["id","name", "prenom","date_birth", "email", "phone", "gps_pos",
                    "nom_societe", "residence", "salaire", "type_contract" ]

class SocieteSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Societe
        fields = ["id", "name", "email", "type_societe", "imatriculation",
                "siege_social", "phone", "gps_pos", "activite", "contrat"]

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