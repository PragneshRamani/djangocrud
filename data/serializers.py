from rest_framework import serializers
from data.models import Information

class InformationSerializer(serializers.ModelSerializer):

        class Meta:
            model = Information
            fields = ['id','first_name','last_name','email','mobile','salary']
