# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsThreatStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribePdnsThreatStatisticsResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribePdnsThreatStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePdnsThreatStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        doh_total_count: int = None,
        domain_count: int = None,
        domain_name: str = None,
        latest_threat_time: int = None,
        max_threat_level: str = None,
        source_ip: str = None,
        sub_domain: str = None,
        threat_level: str = None,
        threat_type: str = None,
        total_count: int = None,
        udp_total_count: int = None,
    ):
        self.doh_total_count = doh_total_count
        self.domain_count = domain_count
        self.domain_name = domain_name
        self.latest_threat_time = latest_threat_time
        self.max_threat_level = max_threat_level
        self.source_ip = source_ip
        self.sub_domain = sub_domain
        self.threat_level = threat_level
        self.threat_type = threat_type
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

        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.latest_threat_time is not None:
            result['LatestThreatTime'] = self.latest_threat_time

        if self.max_threat_level is not None:
            result['MaxThreatLevel'] = self.max_threat_level

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_type is not None:
            result['ThreatType'] = self.threat_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.udp_total_count is not None:
            result['UdpTotalCount'] = self.udp_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DohTotalCount') is not None:
            self.doh_total_count = m.get('DohTotalCount')

        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LatestThreatTime') is not None:
            self.latest_threat_time = m.get('LatestThreatTime')

        if m.get('MaxThreatLevel') is not None:
            self.max_threat_level = m.get('MaxThreatLevel')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatType') is not None:
            self.threat_type = m.get('ThreatType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UdpTotalCount') is not None:
            self.udp_total_count = m.get('UdpTotalCount')

        return self

