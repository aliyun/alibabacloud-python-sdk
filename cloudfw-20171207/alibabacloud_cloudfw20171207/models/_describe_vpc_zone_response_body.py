# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcZoneResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zone_list: List[main_models.DescribeVpcZoneResponseBodyZoneList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The zones.
        self.zone_list = zone_list

    def validate(self):
        if self.zone_list:
            for v1 in self.zone_list:
                 if v1:
                    v1.validate()

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
                result['ZoneList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.zone_list = []
        if m.get('ZoneList') is not None:
            for k1 in m.get('ZoneList'):
                temp_model = main_models.DescribeVpcZoneResponseBodyZoneList()
                self.zone_list.append(temp_model.from_map(k1))

        return self

class DescribeVpcZoneResponseBodyZoneList(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
        zone_type: str = None,
    ):
        # The name of the zone.
        self.local_name = local_name
        # The zone ID.
        self.zone_id = zone_id
        # The zone type. Default value: AvailabilityZone. This value indicates Alibaba Cloud zones.
        self.zone_type = zone_type

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

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

