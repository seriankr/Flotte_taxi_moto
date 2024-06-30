from rest_framework import serializers
from .models import Chauffeur

class ChauffeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = ['id','utilisteur','contrat_type','created_by','modified_by']

    def validate_utilisteur(self, value):
        if not value:
            raise serializers.ValidationError("L'utilisateur est requis.")
        return value

