# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailabilityZonesResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: List[main_models.DescribeAvailabilityZonesResponseBodyAvailableZones] = None,
        request_id: str = None,
    ):
        # The details of the zones where resources are available for purchase.
        self.available_zones = available_zones
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_zones:
            for v1 in self.available_zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableZones'] = []
        if self.available_zones is not None:
            for k1 in self.available_zones:
                result['AvailableZones'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zones = []
        if m.get('AvailableZones') is not None:
            for k1 in m.get('AvailableZones'):
                temp_model = main_models.DescribeAvailabilityZonesResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailabilityZonesResponseBodyAvailableZones(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the region ID.
        self.region_id = region_id
        # The zone ID.
        self.zone_id = zone_id
        # The zone name.
        # 
        # The returned language is determined by the **AcceptLanguage** parameter. Take the **cn-hangzhou-h** zone as an example:
        # 
        # - If **AcceptLanguage** is set to **zh**: 杭州 可用区H
        # - If **AcceptLanguage** is set to **en**: Hangzhou Zone H
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

