# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsRequestStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribePdnsRequestStatisticResponseBodyData] = None,
        request_id: str = None,
    ):
        # The statistics on the DNS requests.
        self.data = data
        # The request ID.
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
                temp_model = main_models.DescribePdnsRequestStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePdnsRequestStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        doh_total_count: int = None,
        http_count: int = None,
        https_count: int = None,
        ip_count: int = None,
        timestamp: int = None,
        total_count: int = None,
        udp_total_count: int = None,
        v_4count: int = None,
        v_4http_count: int = None,
        v_4https_count: int = None,
        v_6count: int = None,
        v_6http_count: int = None,
        v_6https_count: int = None,
    ):
        # The total number of DoH requests, including HTTP and HTTPS requests.
        self.doh_total_count = doh_total_count
        # The number of HTTP requests.
        self.http_count = http_count
        # The number of HTTPS requests. On the Traffic Analysis tab of the Public DNS console, the value of this parameter includes the number of DNS over HTTPs (DoH) requests. Therefore, the number of DoH requests is not separately displayed in the console.
        self.https_count = https_count
        # The number of source IP addresses.
        self.ip_count = ip_count
        # The statistical timestamp. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doh_total_count is not None:
            result['DohTotalCount'] = self.doh_total_count

        if self.http_count is not None:
            result['HttpCount'] = self.http_count

        if self.https_count is not None:
            result['HttpsCount'] = self.https_count

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

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

        if m.get('HttpCount') is not None:
            self.http_count = m.get('HttpCount')

        if m.get('HttpsCount') is not None:
            self.https_count = m.get('HttpsCount')

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

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

