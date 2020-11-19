from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import AgLitterSerializer, HerdSerializer, AgParitySerializer
from .models import AgLitter, AgParity, Herd
from rest_framework.response import Response

class AgLitterViewSet(viewsets.ViewSet):
    def create(self, request, format=None):
        return Response({
            "Error": "Not supported"
        }, 405)

    def get(self, request):
        agLitters = AgLitter.objects.all().order_by('litter_id')
        content = []
        print("get")
        for aglitter in agLitters:
            content.append(self.format_row(aglitter))
        return Response(content, 200)

    def format_row(self, row):
        return {
            'litter_id': row.litter_id,
            'beginlitdate': row.beginlitdate,
            'fosteron': row.fosteron,
            'fosteroff': row.fosteroff,
            'deaths': row.deaths,
            'totalwean': row.totalwean,
            'weandate': row.weandate,
            'iid_parity': row.iid_parity.id,
            'fk_wean_event': row.fk_wean_event,
            'fk_begin_event': row.fk_begin_event,
            'herd': row.herd_id,
            'weanlocation': row.weanlocation,
            'weanloc1': row.weanloc1,
            'weanloc2': row.weanloc2,
            'nurseonage': row.nurseonage
        }

    def create(self, request):
        data_id = request.data["litter_id"]
        data_beginlitdate = request.data["heo_con"]

        for d in data_beginlitdate:
            print(d['id'])

        # data_fosteron = request.data["fosteron"]
        # data_fosteroff = request.data["fosteroff"]
        # data_deaths = request.data["deaths"]
        # data_totalwean = request.data["totalwean"]
        # data_weandate = request.data["weandate"]
        # data_iid_parity = request.data["iid_parity"]
        # data_fk_wean_event = request.data["fk_wean_event"]
        # data_fk_begin_event = request.data["fk_begin_event"]
        # data_herd = request.data["herd"]
        # data_weanlocation = request.data["weanlocation"]
        # data_weanloc1 = request.data["weanloc1"]
        # data_weanloc2 = request.data["weanloc2"]
        # data_nurseonage = request.data["nurseonage"]

        # AgLitter.objects.update_or_create(
        #     litter_id=data_id,
        #     beginlitdate=data_beginlitdate,
        #     fosteron=data_fosteron,
        #     fosteroff=data_fosteroff,
        #     deaths=data_deaths,
        #     totalwean=data_totalwean,
        #     weandate=data_weandate,
        #     iid_parity=AgParity(id=data_iid_parity),
        #     fk_wean_event=data_fk_wean_event,
        #     fk_begin_event=data_fk_begin_event,
        #     herd=Herd(herd_id=data_herd),
        #     weanlocation=data_weanlocation,
        #     weanloc1=data_weanloc1,
        #     weanloc2=data_weanloc2,
        #     nurseonage=data_nurseonage,
        # )
        # print(request.data)
        # post_data = request.data['iid_parity']
        # print(post_data)
        # p = AgLitter.objects.create(litter_id="post_data")
        return Response("post ok")
