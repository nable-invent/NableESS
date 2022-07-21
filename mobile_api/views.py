
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from master.models import Company,Contact,Individual,Pipeline
from mobile_api.serializers import ContactSerializers,CompanySerializers,IndividualSerializers,PipelineSerializers
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status


class SaveContact(APIView):
    # parser_classes = (MultiPartParser, FormParser)
    def post(self,request):
        if request.data['user_type'] == "individual":
            print(request.data['user_type'])
            individual = IndividualSerializers(data=request.data)
            contact = ContactSerializers(data=request.data)
            if individual.is_valid() and contact.is_valid():
                # individual.save()
                # contact.save()
                return Response(individual.data,status=status.HTTP_201_CREATED) 
            else:
                message = {"error": individual.errors}
                message = {"error": contact.errors}
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
        else:
            print(request.data['user_type'])
            company = CompanySerializers(data=request.data)
            contact1 = ContactSerializers(data=request.data)
            if company.is_valid() and contact1.is_valid():
                # company.save()
                # contact1.save()
                return Response(contact1.data,status=status.HTTP_201_CREATED)
            else:
                message = {"error": company.errors}
                message = {"error": contact1.errors}
                return Response(message,status=status.HTTP_400_BAD_REQUEST)


class ContactList(APIView):
    def get(self,request):
        qs = Contact.objects.all()
        contact = ContactSerializers(qs, many=True)       
        return Response(contact.data,status=status.HTTP_200_OK)


class GetContact(APIView):
    def get(self,request,id):
        try:
            res = Contact.objects.get(id=id)
            return Response(ContactSerializers(res).data,status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            message = {"error":"Invalid Contact"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)


class UpdateContact(APIView):
    def put(self,request,id):
        try:
            res = Contact.objects.get(id=id)
            contact = ContactSerializers(res,request.data,partial=True)
            if contact.is_valid():
                contact.save()
                return Response(contact.data,status=status.HTTP_201_CREATED)
            else:
                return Response(contact.errors,status=status.HTTP_404_NOT_FOUND)
        except Contact.DoesNotExist:
            message = {"error":"Invalid Contact"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)   


class DeleteContact(APIView):
    def delete(self,request,id):
        res = Contact.objects.filter(id=id).delete()
        if res[0]!=0:
            message = {"message":"Contact Is Deleted"}
            return Response(message,status=status.HTTP_200_OK)
        else:
            message = {"error":"Invalid Contact"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)


class SavePipeline(APIView):
    def post(self,request):
        pipeline = PipelineSerializers(data=request.data)
        if pipeline.is_valid():
            #pipeline.save()
            print(request.data)
            return Response(pipeline.data,status=status.HTTP_201_CREATED)
        else:
            return Response(pipeline.errors,status=status.HTTP_400_BAD_REQUEST)