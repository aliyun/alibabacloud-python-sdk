# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsThreatStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribePdnsThreatStatisticResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribePdnsThreatStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePdnsThreatStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        doh_total_count: int = None,
        threat_level: str = None,
        threat_type: str = None,
        timestamp: int = None,
        total_count: int = None,
        udp_total_count: int = None,
    ):
        self.doh_total_count = doh_total_count
        self.threat_level = threat_level
        self.threat_type = threat_type
        self.timestamp = timestamp
        self.total_count = total_count
        self.udp_total_count = udp_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doh_total_count is not None:
            result['DohTotalCount'] = self.doh_total_count

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_type is not None:
            result['ThreatType'] = self.threat_type

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.udp_total_count is not None:
            result['UdpTotalCount'] = self.udp_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DohTotalCount') is not None:
            self.doh_total_count = m.get('DohTotalCount')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatType') is not None:
            self.threat_type = m.get('ThreatType')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UdpTotalCount') is not None:
            self.udp_total_count = m.get('UdpTotalCount')

        return self

