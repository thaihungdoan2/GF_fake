from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Vaccine, Tiemphong
from fakeheo.models import HeoAll
from rest_framework.response import Response

class VaccineViewSet(viewsets.ViewSet):
    def create(self, request, format=None):
        return Response({
            "Error": "Not supported"
        }, 405)

    def get(self, request):
        vaccines = Vaccine.objects.all().order_by('id_vaccine')
        content = []
        print("get")
        for vaccine in vaccines:
            content.append(self.format_row(vaccine))
        return Response(content, 200)

    def format_row(self, row):
        return {
            'name_vaccine': row.name_vaccine,
        }

    def create(self, request):
        data_rfid = request.data["rfid"]
        data_vaccine = request.data["name_vaccine"]
        heo_rfids = HeoAll.objects.all()
        for heo_rfid in heo_rfids:
            print(len(heo_rfid.rfid))
            print(len(data_rfid))
            if data_rfid == heo_rfid.rfid:
                print("ok rfid")
                Tiemphong.objects.update_or_create(
                    Vaccine=Vaccine(id_vaccine=data_vaccine),
                    RFID=HeoAll(rfid=data_rfid)
                )
        print("ok vaccine")
        # post_data = request.data['iid_parity']
        # print(post_data)
        # p = AgLitter.objects.create(litter_id="post_data")
        return Response("post ok")
