# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessInstanceZoneListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zone_list: List[str] = None,
        zones: List[main_models.DescribeAccessInstanceZoneListResponseBodyZones] = None,
    ):
        self.request_id = request_id
        self.zone_list = zone_list
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.zone_list is not None:
            result['ZoneList'] = self.zone_list

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ZoneList') is not None:
            self.zone_list = m.get('ZoneList')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.DescribeAccessInstanceZoneListResponseBodyZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class DescribeAccessInstanceZoneListResponseBodyZones(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

