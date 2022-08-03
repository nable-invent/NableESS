
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from master.models import Company,Contact,Individual,Pipeline
from mobile_api.serializers import ContactSerializers,CompanySerializers,IndividualSerializers,PipelineSerializers
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status
import json


class SaveContact(APIView):

    def post(self,request):
        if request.data['user_type'] == "individual":
            print(request.data['user_type'])
            individual = IndividualSerializers(data=request.data)
            # contact = ContactSerializers(data=request.data)
            var = Company.objects.get(id=request.data["company_name"])
            if individual.is_valid():
                idata = individual.save()
                print("Idata",idata)
                print("Indivisual Data Is Saved")
                id = Individual.objects.get(id=idata.id)
                data = Contact.objects.create(name=request.data['name'],company_name=var,
                individual=id,mobile=request.data['mobile'],email=request.data['email'],
          
               )
                data.save()
                print("Contact Data Is Saved")
                return Response(individual.data,status=status.HTTP_201_CREATED) 
            else:
                # message = {"error": individual.errors}
                return Response(individual.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            print(request.data['user_type'])
            company = CompanySerializers(data=request.data)
            if company.is_valid():
                cdata = company.save()
                print("Company Data is Saved")
                cid = Company.objects.get(id=cdata.id)
                condata = Contact.objects.create(cmp_title=request.data['name'],company=cid,
                cmp_mobile=request.data['mobile'],cmp_email=request.data['email'])
                condata.save()
                print("Contact Data is Saved")
                return Response(company.data,status=status.HTTP_201_CREATED)
            else:
                # message = {"error": company.errors}
                return Response(company.errors,status=status.HTTP_400_BAD_REQUEST)


class CompanyList(APIView):
    def get(self,request):
        qs = Company.objects.all()
        company = CompanySerializers(qs, many=True)       
        return Response(company.data,status=status.HTTP_200_OK)


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
    parser_classes = (MultiPartParser, FormParser)
    def put(self,request,id):
        if request.data['user_type'] == "individual":
            print(request.data['user_type'])
            try:
                res = Contact.objects.get(id=id)
                idata = Individual.objects.get(id=res.individual.id)
                var = Company.objects.get(id=request.data["company_name"])
                individual = IndividualSerializers(idata,request.data,partial=True)
                if individual.is_valid():
                    data = individual.save()
                    print("Individual Data is Saved")
                    res.name=request.data['name']
                    res.title=request.data['title']
                    res.company_name=var
                    res.individual=data
                    res.tax_id=request.data['tax_id']
                    res.address_street_1=request.data['address_street_1']
                    res.address_street_2=request.data['address_street_2']
                    res.city=request.data['city']
                    res.state=request.data['state']
                    res.country=request.data['country']
                    res.zip_code=request.data['zip_code']
                    res.job_position=request.data['job_position']
                    res.phone=request.data['phone']
                    res.mobile=request.data['mobile']
                    res.email=request.data['email']
                    res.website=request.data['website']
                    res.tags=request.data['tags']
                    res.image=request.data['image']
                    res.internal_notes=request.data['internal_notes']
                    res.sales_person=request.data['sales_person']
                    res.refrence=request.data['refrence']
                    res.save()
                    print("contact data is saved")
                    return Response(individual.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(individual.errors,status=status.HTTP_404_NOT_FOUND)
            except Contact.DoesNotExist:
                message = {"error":"Invalid Contact"}
                return Response(message,status=status.HTTP_404_NOT_FOUND)
        else:   
            print(request.data['user_type'])
            try:
                cres = Contact.objects.get(id=id)
                cid = Company.objects.get(id=cres.company.id)
                company = CompanySerializers(cid,request.data,partial=True)
                if company.is_valid():
                    company.save()
                    print("Company Data is Saved")
                    cres.cmp_title=request.data['name']
                    cres.cmp_tax_id=request.data['tax_id']
                    cres.company=cid
                    cres.cmp_address_street_1=request.data['address_street_1']
                    cres.cmp_address_street_2=request.data['address_street_2']
                    cres.cmp_city=request.data['city']
                    cres.cmp_state=request.data['state']
                    cres.cmp_country=request.data['country']
                    cres.cmp_zip_code=request.data['zip_code']
                    cres.cmp_phone=request.data['phone']
                    cres.cmp_mobile=request.data['mobile']
                    cres.cmp_email=request.data['email']
                    cres.cmp_website=request.data['website']
                    cres.cmp_tags=request.data['tags']
                    cres.company_image=request.data['image']
                    cres.cmp_internal_notes=request.data['internal_notes']
                    cres.cmp_sales_person=request.data['sales_person']
                    cres.cmp_refrence=request.data['refrence']
                    cres.cmp_industry=request.data['industry']
                    cres.save()
                    print("Contact data is saved")
                    return Response(company.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(individual.errors,status=status.HTTP_404_NOT_FOUND)
            except Contact.DoesNotExist:
                message = {"error":"Invalid Contact"}
                return Response(message,status=status.HTTP_404_NOT_FOUND)



class DeleteContact(APIView):
    def delete(self,request,id):
        try:
            data = Contact.objects.get(id=id)
            cdata = data.cmp_title
            if cdata:
                print("Company")
                cid = data.company.id
                Company.objects.filter(id=cid).delete()
                print("Company Delete")
                Contact.objects.filter(id=id).delete()
                print("Contact Delete")
                message = {"message":"Contact Is Deleted"}
                return Response(message,status=status.HTTP_204_NO_CONTENT)
            else:
                print("Indivisual")
                iid = data.individual.id
                Individual.objects.filter(id=iid).delete()
                print("Individual Delete")
                Contact.objects.filter(id=id).delete()
                message = {"message":"Contact Is Deleted"}
                return Response(message,status=status.HTTP_204_NO_CONTENT)
        except:
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


class PipelineList(APIView):
    def get(self,request):
        qs = Pipeline.objects.all()
        pipeline = PipelineSerializers(qs, many=True)       
        return Response(pipeline.data,status=status.HTTP_200_OK)



class GetPipeline(APIView):
    def get(self,request,id):
        try:
            res = Pipeline.objects.get(id=id)
            return Response(PipelineSerializers(res).data,status=status.HTTP_200_OK)
        except Pipeline.DoesNotExist:
            message = {"error":"Invalid Pipeline"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)


class UpdatePipeline(APIView):
    def put(self,request,id):
        try:
            res = Pipeline.objects.get(id=id)
            print("RES",res)
            pipeline = PipelineSerializers(res,request.data,partial=True)
            if pipeline.is_valid():
                #pipeline.save()
                return Response(pipeline.data,status=status.HTTP_201_CREATED)
            else:
                return Response(pipeline.errors,status=status.HTTP_400_BAD_REQUEST)
        except Pipeline.DoesNotExist:
            message = {"error":"Invalid Pipeline"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)


class DeletePipeline(APIView):
    def delete(self,request,id):
        res = Pipeline.objects.filter(id=id).delete()
        if res[0]!=0:
            message = {"message":"Contact Is Deleted"}
            return Response(message,status=status.HTTP_204_NO_CONTENT)
        else:
            message = {"error":"Invalid Contact"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)