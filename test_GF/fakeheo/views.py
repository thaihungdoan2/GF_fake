from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import HeoMe, HeoCon
from rest_framework.response import Response


class HeoMeViewSet(viewsets.ViewSet):
    def create(self, request, format=None):
        return Response({
            "Error": "Not supported"
        }, 405)

    def get(self, request):
        heomes = HeoMe.objects.all().order_by('id')
        content = []
        print("get")
        for heome in heomes:
            content.append(self.format_row(heome))
        return Response(content, 200)

    def format_row(self, row):
        return {
            # 'id': row.id,
            'name_heome': row.name_heome,
            'rfid_heome': row.rfid_heome,
            'chuong': row.chuong,
        }

    def create(self, request):
        # data_id = request.data["id"]
        data_name_heome = request.data["name_heome"]
        data_rfid_heome = request.data["rfid_heome"]
        data_chuong = request.data["chuong"]

        HeoMe.objects.update_or_create(
            id=data_id,
            name_heome=data_name_heome,
            rfid_heome=data_rfid_heome,
            chuong=data_chuong,
        )
        # print(request.data)
        # post_data = request.data['iid_parity']
        # print(post_data)
        # p = AgLitter.objects.create(litter_id="post_data")
        return Response("post ok")


class HeoconViewSet(viewsets.ViewSet):
    def create(self, request, format=None):
        return Response({
            "Error": "Not supported"
        }, 405)

    def get(self, request):
        heocons = HeoCon.objects.all()
        content1 = []
        print("get_heocon")
        for heocon in heocons:
            content1.append(self.format_row(heocon))
        return Response(content1, 200)

    def format_row(self, row):
        # print(row.id_heome)
        return {
            # 'id_heocon': row.id_heocon,
            'id_heome': row.rfid_heome,
            'weight': row.weight,
            'rfid_heocon': row.rfid_heocon,
        }

    def create(self, request):
        # data_id_heocon = request.data["id_heocon"]
        data_id_heome = request.data["id_heome"]
        data_weight = request.data["weight"]
        data_rfid_heocon = request.data["rfid_heocon"]

        HeoCon.objects.update_or_create(
            id_heocon=data_id_heocon,
            id_heome=HeoMe(id=data_id_heome),
            weight=data_weight,
            rfid_heocon=data_rfid_heocon,
        )
        return Response("post ok")


class HeoallViewSet(viewsets.ViewSet):
    def create(self, request, format=None):
        return Response({
            "Error": "Not supported"
        }, 405)

    def get(self, request, format=None):
        heome_id = request.query_params.get('rfid_heome')
        if heome_id == None:
            return Response({
                "error": "no params"
            }, 200)
        heomes = HeoMe.objects.filter(rfid_heome=heome_id)
        content1 = []
        print("get_all")
        for heocon in heomes:
            content1.append(self.format_row(heocon))

        return Response(content1, 200)

    def format_row(self, row):
        return {
            'id_heome': row.rfid_heome,
            'name_heome': row.name_heome,
            'chuong': row.chuong
        }

    def create(self, request):
        data_id_heome = request.data["rfid_heome"]
        data_id_heocon = request.data["id_heocon"]
        # print(request.data['rfid_heome'])
        for d in data_id_heocon:
            data_heocon_weight = d['weight']
            data_heocon_rfid = d['rfid']
            # print(data_id_heome)
            # print(data_heocon_weight)
            # print(data_heocon_rfid)
            # print("----------------------------------")
            HeoCon.objects.update_or_create(
                # id_heome=HeoMe(rfid_heome=data_id_heome),
                rfid_heome=data_id_heome,
                weight=data_heocon_weight,
                rfid_heocon=data_heocon_rfid,
            )

        return Response("post ok")
