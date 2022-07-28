from  master.models import Company,Contact,Individual,Pipeline
from rest_framework import serializers


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class IndividualSerializers(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = "__all__"
        

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
        depth = 2


class PipelineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pipeline
        fields = "__all__"
        depth = 2
