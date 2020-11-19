from rest_framework import serializers

from .models import AgLitter, AgParity, Herd


class HerdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herd
        fields = ['herd_id']

class AgParitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgParity
        fields = ['iid_nextparity']


class AgLitterSerializer(serializers.ModelSerializer):
    herd = HerdSerializer()
    iid_parity = AgParitySerializer()
    class Meta:
        model = AgLitter
        fields = ['litter_id', 'beginlitdate',
                  'fosteron', 'fosteroff', 'deaths', 'totalwean', 'weandate', 'iid_parity',
                  'fk_wean_event', 'fk_begin_event', 'weanlocation', 'weanloc1', 'herd',
                  'weanloc2', 'nurseonage']
