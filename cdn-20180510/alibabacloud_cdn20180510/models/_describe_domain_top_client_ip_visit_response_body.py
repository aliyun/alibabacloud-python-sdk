# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainTopClientIpVisitResponseBody(DaraModel):
    def __init__(
        self,
        client_ip_list: List[main_models.DescribeDomainTopClientIpVisitResponseBodyClientIpList] = None,
        request_id: str = None,
    ):
        # A list of client IP addresses.
        self.client_ip_list = client_ip_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.client_ip_list:
            for v1 in self.client_ip_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClientIpList'] = []
        if self.client_ip_list is not None:
            for k1 in self.client_ip_list:
                result['ClientIpList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_ip_list = []
        if m.get('ClientIpList') is not None:
            for k1 in m.get('ClientIpList'):
                temp_model = main_models.DescribeDomainTopClientIpVisitResponseBodyClientIpList()
                self.client_ip_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainTopClientIpVisitResponseBodyClientIpList(DaraModel):
    def __init__(
        self,
        acc: int = None,
        client_ip: str = None,
        rank: int = None,
        traffic: int = None,
    ):
        # The total number of requests.
        self.acc = acc
        # The client IP address returned. Only IPv4 addressed are supported.
        self.client_ip = client_ip
        # The ranking of the client IP address returned.
        self.rank = rank
        # The total amount of network traffic consumed. Unit: bytes.
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acc is not None:
            result['Acc'] = self.acc

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.rank is not None:
            result['Rank'] = self.rank

        if self.traffic is not None:
            result['Traffic'] = self.traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Rank') is not None:
            self.rank = m.get('Rank')

        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')

        return self

