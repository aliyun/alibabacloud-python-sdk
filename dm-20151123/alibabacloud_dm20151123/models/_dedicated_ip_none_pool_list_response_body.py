# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class DedicatedIpNonePoolListResponseBody(DaraModel):
    def __init__(
        self,
        ips: List[main_models.DedicatedIpNonePoolListResponseBodyIps] = None,
        request_id: str = None,
    ):
        # Information on IPs not added to the IP pool
        self.ips = ips
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.ips:
            for v1 in self.ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ips'] = []
        if self.ips is not None:
            for k1 in self.ips:
                result['Ips'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ips = []
        if m.get('Ips') is not None:
            for k1 in m.get('Ips'):
                temp_model = main_models.DedicatedIpNonePoolListResponseBodyIps()
                self.ips.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DedicatedIpNonePoolListResponseBodyIps(DaraModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        zone_id: str = None,
    ):
        # Purchased instance ID
        self.id = id
        # IP address
        self.ip = ip
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

