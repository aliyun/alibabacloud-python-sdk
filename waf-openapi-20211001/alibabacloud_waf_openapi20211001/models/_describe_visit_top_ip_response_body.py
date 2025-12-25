# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeVisitTopIpResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        top_ip: List[main_models.DescribeVisitTopIpResponseBodyTopIp] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The array of the top 10 IP addresses from which requests are sent.
        self.top_ip = top_ip

    def validate(self):
        if self.top_ip:
            for v1 in self.top_ip:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TopIp'] = []
        if self.top_ip is not None:
            for k1 in self.top_ip:
                result['TopIp'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.top_ip = []
        if m.get('TopIp') is not None:
            for k1 in m.get('TopIp'):
                temp_model = main_models.DescribeVisitTopIpResponseBodyTopIp()
                self.top_ip.append(temp_model.from_map(k1))

        return self

class DescribeVisitTopIpResponseBodyTopIp(DaraModel):
    def __init__(
        self,
        area: str = None,
        count: int = None,
        ip: str = None,
        isp: str = None,
    ):
        # The ordinal number of the area to which the IP address belongs.
        self.area = area
        # The total number of requests that are sent from the IP address.
        self.count = count
        # The IP address.
        self.ip = ip
        # The ISP.
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.count is not None:
            result['Count'] = self.count

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.isp is not None:
            result['Isp'] = self.isp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        return self

