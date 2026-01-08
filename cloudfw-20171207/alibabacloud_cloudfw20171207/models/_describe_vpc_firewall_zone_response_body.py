# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallZoneResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zone_list: List[List[main_models.DescribeVpcFirewallZoneResponseBodyZoneList]] = None,
    ):
        self.request_id = request_id
        self.zone_list = zone_list

    def validate(self):
        if self.zone_list:
            for v1 in self.zone_list:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ZoneList'] = []
        if self.zone_list is not None:
            for k1 in self.zone_list:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['ZoneList'].append(l1)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.zone_list = []
        if m.get('ZoneList') is not None:
            for k1 in m.get('ZoneList'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.DescribeVpcFirewallZoneResponseBodyZoneList()
                    l1.append(temp_model.from_map(k2))
                self.zone_list.append(l1)

        return self

class DescribeVpcFirewallZoneResponseBodyZoneList(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
        local_name: str = None,
    ):
        self.zone_id = zone_id
        self.local_name = local_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        return self

