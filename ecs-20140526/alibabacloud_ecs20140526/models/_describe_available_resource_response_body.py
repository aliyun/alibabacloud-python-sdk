# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableResourceResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: main_models.DescribeAvailableResourceResponseBodyAvailableZones = None,
        request_id: str = None,
    ):
        # The information about the availability of resources in the zones.
        self.available_zones = available_zones
        self.request_id = request_id

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m.get('AvailableZones'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailableResourceResponseBodyAvailableZones(DaraModel):
    def __init__(
        self,
        available_zone: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone] = None,
    ):
        self.available_zone = available_zone

    def validate(self):
        if self.available_zone:
            for v1 in self.available_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k1 in self.available_zone:
                result['AvailableZone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k1 in m.get('AvailableZone'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone(DaraModel):
    def __init__(
        self,
        available_resources: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources = None,
        region_id: str = None,
        status: str = None,
        status_category: str = None,
        zone_id: str = None,
    ):
        self.available_resources = available_resources
        self.region_id = region_id
        self.status = status
        # The resource status based on the stock level in the zone. Valid value:
        # 
        # *   WithStock: The resources are available and can be continuously replenished.
        # *   ClosedWithStock: Inventory is available, but resources will not be replenished. The ability to guarantee the supply of inventory is low. We recommend selecting a product specification in the WithStock state.
        # *   WithoutStock: The resource is out of stock and will be replenished. We recommend using other resources that are in stock.
        # *   ClosedWithoutStock: The resource is out of stock and will no longer be replenished. We recommend using other resources that are in stock.
        self.status_category = status_category
        self.zone_id = zone_id

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()

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
        if m.get('AvailableResources') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources()
            self.available_resources = temp_model.from_map(m.get('AvailableResources'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCategory') is not None:
            self.status_category = m.get('StatusCategory')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources(DaraModel):
    def __init__(
        self,
        available_resource: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource] = None,
    ):
        self.available_resource = available_resource

    def validate(self):
        if self.available_resource:
            for v1 in self.available_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableResource'] = []
        if self.available_resource is not None:
            for k1 in self.available_resource:
                result['AvailableResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resource = []
        if m.get('AvailableResource') is not None:
            for k1 in m.get('AvailableResource'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource(DaraModel):
    def __init__(
        self,
        supported_resources: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources = None,
        type: str = None,
    ):
        self.supported_resources = supported_resources
        self.type = type

    def validate(self):
        if self.supported_resources:
            self.supported_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_resources is not None:
            result['SupportedResources'] = self.supported_resources.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedResources') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources()
            self.supported_resources = temp_model.from_map(m.get('SupportedResources'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources(DaraModel):
    def __init__(
        self,
        supported_resource: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource] = None,
    ):
        self.supported_resource = supported_resource

    def validate(self):
        if self.supported_resource:
            for v1 in self.supported_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedResource'] = []
        if self.supported_resource is not None:
            for k1 in self.supported_resource:
                result['SupportedResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource = []
        if m.get('SupportedResource') is not None:
            for k1 in m.get('SupportedResource'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource()
                self.supported_resource.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource(DaraModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
        status: str = None,
        status_category: str = None,
        unit: str = None,
        value: str = None,
    ):
        self.max = max
        self.min = min
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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCategory') is not None:
            self.status_category = m.get('StatusCategory')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

