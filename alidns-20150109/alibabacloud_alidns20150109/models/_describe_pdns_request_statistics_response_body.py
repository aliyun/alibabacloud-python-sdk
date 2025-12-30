# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsRequestStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribePdnsRequestStatisticsResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The statistics on the DNS requests.
        self.data = data
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **20**. Valid values: **1 to 100**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = main_models.DescribePdnsRequestStatisticsResponseBodyData()
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

class DescribePdnsRequestStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        doh_total_count: int = None,
        domain_name: str = None,
        http_count: int = None,
        https_count: int = None,
        ip_count: int = None,
        max_threat_level: str = None,
        sub_domain: str = None,
        threat_count: int = None,
        threat_info: List[main_models.DescribePdnsRequestStatisticsResponseBodyDataThreatInfo] = None,
        total_count: int = None,
        udp_total_count: int = None,
        v_4count: int = None,
        v_4http_count: int = None,
        v_4https_count: int = None,
        v_6count: int = None,
        v_6http_count: int = None,
        v_6https_count: int = None,
    ):
        # The total number of DoH requests, including the HTTP and HTTPS requests.
        self.doh_total_count = doh_total_count
        # The domain name.
        self.domain_name = domain_name
        # The number of HTTP requests.
        self.http_count = http_count
        # The number of HTTPS requests. On the Traffic Analysis tab of the public DNS console, the value of this parameter includes the number of DNS over HTTPs (DoH) requests. Therefore, the number of DoH requests is not separately displayed in the console.
        self.https_count = https_count
        # The number of source IP addresses.
        self.ip_count = ip_count
        # The current version does not support this parameter.
        self.max_threat_level = max_threat_level
        # The subdomain name.
        self.sub_domain = sub_domain
        # The current version does not support this parameter.
        self.threat_count = threat_count
        # The current version does not support this parameter.
        self.threat_info = threat_info
        # The total number of requests.
        self.total_count = total_count
        # The total number of UDP requests.
        self.udp_total_count = udp_total_count
        # The number of IPv4-based requests.
        self.v_4count = v_4count
        # The number of IPv4-based HTTP requests.
        self.v_4http_count = v_4http_count
        # The number of IPv4-based HTTPS requests.
        self.v_4https_count = v_4https_count
        # The number of IPv6-based requests.
        self.v_6count = v_6count
        # The number of IPv6-based HTTP requests.
        self.v_6http_count = v_6http_count
        # The number of IPv6-based HTTPS requests.
        self.v_6https_count = v_6https_count

    def validate(self):
        if self.threat_info:
            for v1 in self.threat_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doh_total_count is not None:
            result['DohTotalCount'] = self.doh_total_count

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.http_count is not None:
            result['HttpCount'] = self.http_count

        if self.https_count is not None:
            result['HttpsCount'] = self.https_count

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        if self.max_threat_level is not None:
            result['MaxThreatLevel'] = self.max_threat_level

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.threat_count is not None:
            result['ThreatCount'] = self.threat_count

        result['ThreatInfo'] = []
        if self.threat_info is not None:
            for k1 in self.threat_info:
                result['ThreatInfo'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.udp_total_count is not None:
            result['UdpTotalCount'] = self.udp_total_count

        if self.v_4count is not None:
            result['V4Count'] = self.v_4count

        if self.v_4http_count is not None:
            result['V4HttpCount'] = self.v_4http_count

        if self.v_4https_count is not None:
            result['V4HttpsCount'] = self.v_4https_count

        if self.v_6count is not None:
            result['V6Count'] = self.v_6count

        if self.v_6http_count is not None:
            result['V6HttpCount'] = self.v_6http_count

        if self.v_6https_count is not None:
            result['V6HttpsCount'] = self.v_6https_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DohTotalCount') is not None:
            self.doh_total_count = m.get('DohTotalCount')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('HttpCount') is not None:
            self.http_count = m.get('HttpCount')

        if m.get('HttpsCount') is not None:
            self.https_count = m.get('HttpsCount')

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        if m.get('MaxThreatLevel') is not None:
            self.max_threat_level = m.get('MaxThreatLevel')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('ThreatCount') is not None:
            self.threat_count = m.get('ThreatCount')

        self.threat_info = []
        if m.get('ThreatInfo') is not None:
            for k1 in m.get('ThreatInfo'):
                temp_model = main_models.DescribePdnsRequestStatisticsResponseBodyDataThreatInfo()
                self.threat_info.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UdpTotalCount') is not None:
            self.udp_total_count = m.get('UdpTotalCount')

        if m.get('V4Count') is not None:
            self.v_4count = m.get('V4Count')

        if m.get('V4HttpCount') is not None:
            self.v_4http_count = m.get('V4HttpCount')

        if m.get('V4HttpsCount') is not None:
            self.v_4https_count = m.get('V4HttpsCount')

        if m.get('V6Count') is not None:
            self.v_6count = m.get('V6Count')

        if m.get('V6HttpCount') is not None:
            self.v_6http_count = m.get('V6HttpCount')

        if m.get('V6HttpsCount') is not None:
            self.v_6https_count = m.get('V6HttpsCount')

        return self

class DescribePdnsRequestStatisticsResponseBodyDataThreatInfo(DaraModel):
    def __init__(
        self,
        threat_level: str = None,
        threat_type: str = None,
    ):
        # The current version does not support this parameter.
        self.threat_level = threat_level
        # The current version does not support this parameter.
        self.threat_type = threat_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_type is not None:
            result['ThreatType'] = self.threat_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatType') is not None:
            self.threat_type = m.get('ThreatType')

        return self

