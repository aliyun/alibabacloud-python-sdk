# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpnGatewayAvailableZonesResponseBody(DaraModel):
    def __init__(
        self,
        available_zone_id_list: List[main_models.DescribeVpnGatewayAvailableZonesResponseBodyAvailableZoneIdList] = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The zones.
        self.available_zone_id_list = available_zone_id_list
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_zone_id_list:
            for v1 in self.available_zone_id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableZoneIdList'] = []
        if self.available_zone_id_list is not None:
            for k1 in self.available_zone_id_list:
                result['AvailableZoneIdList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone_id_list = []
        if m.get('AvailableZoneIdList') is not None:
            for k1 in m.get('AvailableZoneIdList'):
                temp_model = main_models.DescribeVpnGatewayAvailableZonesResponseBodyAvailableZoneIdList()
                self.available_zone_id_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVpnGatewayAvailableZonesResponseBodyAvailableZoneIdList(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
        zone_name: str = None,
    ):
        # The zone ID.
        self.zone_id = zone_id
        # The zone name.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

