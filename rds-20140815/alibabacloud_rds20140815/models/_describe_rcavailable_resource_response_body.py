# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCAvailableResourceResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: List[main_models.DescribeRCAvailableResourceResponseBodyAvailableZones] = None,
        request_id: str = None,
    ):
        self.available_zones = available_zones
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
                temp_model = main_models.DescribeRCAvailableResourceResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRCAvailableResourceResponseBodyAvailableZones(DaraModel):
    def __init__(
        self,
        available_resources: List[main_models.DescribeRCAvailableResourceResponseBodyAvailableZonesAvailableResources] = None,
        region_id: str = None,
        status: str = None,
        status_category: str = None,
        zone_id: str = None,
    ):
        self.available_resources = available_resources
        self.region_id = region_id
        self.status = status
        self.status_category = status_category
        self.zone_id = zone_id

    def validate(self):
        if self.available_resources:
            for v1 in self.available_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k1 in self.available_resources:
                result['AvailableResources'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_category is not None:
            result['StatusCategory'] = self.status_category

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resources = []
        if m.get('AvailableResources') is not None:
            for k1 in m.get('AvailableResources'):
                temp_model = main_models.DescribeRCAvailableResourceResponseBodyAvailableZonesAvailableResources()
                self.available_resources.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCategory') is not None:
            self.status_category = m.get('StatusCategory')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeRCAvailableResourceResponseBodyAvailableZonesAvailableResources(DaraModel):
    def __init__(
        self,
        supported_resources: List[main_models.DescribeRCAvailableResourceResponseBodyAvailableZonesAvailableResourcesSupportedResources] = None,
        type: str = None,
    ):
        self.supported_resources = supported_resources
        self.type = type

    def validate(self):
        if self.supported_resources:
            for v1 in self.supported_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedResources'] = []
        if self.supported_resources is not None:
            for k1 in self.supported_resources:
                result['SupportedResources'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resources = []
        if m.get('SupportedResources') is not None:
            for k1 in m.get('SupportedResources'):
                temp_model = main_models.DescribeRCAvailableResourceResponseBodyAvailableZonesAvailableResourcesSupportedResources()
                self.supported_resources.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeRCAvailableResourceResponseBodyAvailableZonesAvailableResourcesSupportedResources(DaraModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
        quota_status: str = None,
        status: str = None,
        status_category: str = None,
        unit: str = None,
        value: str = None,
    ):
        self.max = max
        self.min = min
        self.quota_status = quota_status
        self.status = status
        self.status_category = status_category
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.quota_status is not None:
            result['QuotaStatus'] = self.quota_status

        if self.status is not None:
            result['Status'] = self.status

        if self.status_category is not None:
            result['StatusCategory'] = self.status_category

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('QuotaStatus') is not None:
            self.quota_status = m.get('QuotaStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCategory') is not None:
            self.status_category = m.get('StatusCategory')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

