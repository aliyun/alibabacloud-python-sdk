# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveTopDomainsByFlowResponseBody(DaraModel):
    def __init__(
        self,
        domain_count: int = None,
        domain_online_count: int = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        top_domains: main_models.DescribeLiveTopDomainsByFlowResponseBodyTopDomains = None,
    ):
        # The total number of domain names in your account.
        self.domain_count = domain_count
        # The total number of domain names that are in the Enabled state in your account.
        self.domain_online_count = domain_online_count
        # The end of the time range for which data was queried.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range for which data was queried.
        self.start_time = start_time
        # The top domain names ranked by traffic.
        self.top_domains = top_domains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TopDomains') is not None:
            temp_model = main_models.DescribeLiveTopDomainsByFlowResponseBodyTopDomains()
            self.top_domains = temp_model.from_map(m.get('TopDomains'))

        return self

class DescribeLiveTopDomainsByFlowResponseBodyTopDomains(DaraModel):
    def __init__(
        self,
        top_domain: List[main_models.DescribeLiveTopDomainsByFlowResponseBodyTopDomainsTopDomain] = None,
    ):
        self.top_domain = top_domain

    def validate(self):
        if self.top_domain:
            for v1 in self.top_domain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TopDomain'] = []
        if self.top_domain is not None:
            for k1 in self.top_domain:
                result['TopDomain'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.top_domain = []
        if m.get('TopDomain') is not None:
            for k1 in m.get('TopDomain'):
                temp_model = main_models.DescribeLiveTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k1))

        return self

class DescribeLiveTopDomainsByFlowResponseBodyTopDomainsTopDomain(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        max_bps: int = None,
        max_bps_time: str = None,
        rank: int = None,
        total_access: int = None,
        total_traffic: str = None,
        traffic_percent: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The peak bandwidth of the domain name.
        self.max_bps = max_bps
        # The time when the bandwidth reached the peak value.
        self.max_bps_time = max_bps_time
        # The ranking of the domain name.
        self.rank = rank
        # The number of visits to the domain name.
        self.total_access = total_access
        # The total traffic.
        self.total_traffic = total_traffic
        # The traffic share of the domain name relative to the total traffic.
        self.traffic_percent = traffic_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps

        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time

        if self.rank is not None:
            result['Rank'] = self.rank

        if self.total_access is not None:
            result['TotalAccess'] = self.total_access

        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic

        if self.traffic_percent is not None:
            result['TrafficPercent'] = self.traffic_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')

        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')

        if m.get('Rank') is not None:
            self.rank = m.get('Rank')

        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')

        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')

        if m.get('TrafficPercent') is not None:
            self.traffic_percent = m.get('TrafficPercent')

        return self

