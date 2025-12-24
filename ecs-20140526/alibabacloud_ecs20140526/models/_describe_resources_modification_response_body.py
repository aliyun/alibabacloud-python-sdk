# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeResourcesModificationResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: main_models.DescribeResourcesModificationResponseBodyAvailableZones = None,
        request_id: str = None,
    ):
        # The information about the queried zones.
        self.available_zones = available_zones
        # The request ID.
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
            temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m.get('AvailableZones'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeResourcesModificationResponseBodyAvailableZones(DaraModel):
    def __init__(
        self,
        available_zone: List[main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZone] = None,
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
                temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k1))

        return self

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZone(DaraModel):
    def __init__(
        self,
        available_resources: main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResources = None,
        region_id: str = None,
        status: str = None,
        status_category: str = None,
        zone_id: str = None,
    ):
        # The resources that are available in the zone.
        self.available_resources = available_resources
        # The region ID.
        self.region_id = region_id
        # The state of the resource. Valid values:
        # 
        # *   Available
        # *   SoldOut
        self.status = status
        # The category of the resource based on stock status. Valid values:
        # 
        # *   WithStock: resources that are in sufficient stock
        # *   ClosedWithStock: resources that are in insufficient stock
        # *   WithoutStock: resources that are out of stock
        self.status_category = status_category
        # The zone ID.
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
            temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResources()
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

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResources(DaraModel):
    def __init__(
        self,
        available_resource: List[main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource] = None,
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
                temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k1))

        return self

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource(DaraModel):
    def __init__(
        self,
        condition_supported_resources: main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResources = None,
        supported_resources: main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources = None,
        type: str = None,
    ):
        # The resource types that resources can be changed to after the resources meet specified conditions. If the conditions are met, you can change the current resource to a resource in the list.
        self.condition_supported_resources = condition_supported_resources
        # The information about the supported resources.
        self.supported_resources = supported_resources
        # The resource type. Valid values:
        # 
        # *   InstanceType
        # *   SystemDisk
        self.type = type

    def validate(self):
        if self.condition_supported_resources:
            self.condition_supported_resources.validate()
        if self.supported_resources:
            self.supported_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_supported_resources is not None:
            result['ConditionSupportedResources'] = self.condition_supported_resources.to_map()

        if self.supported_resources is not None:
            result['SupportedResources'] = self.supported_resources.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionSupportedResources') is not None:
            temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResources()
            self.condition_supported_resources = temp_model.from_map(m.get('ConditionSupportedResources'))

        if m.get('SupportedResources') is not None:
            temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources()
            self.supported_resources = temp_model.from_map(m.get('SupportedResources'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources(DaraModel):
    def __init__(
        self,
        supported_resource: List[main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource] = None,
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
                temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource()
                self.supported_resource.append(temp_model.from_map(k1))

        return self

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource(DaraModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
        status: str = None,
        status_category: str = None,
        unit: str = None,
        value: str = None,
    ):
        # The maximum disk capacity.
        # 
        # This parameter takes effect only when the DestinationResource request parameter is set to SystemDisk.
        self.max = max
        # The minimum disk capacity.
        # 
        # This parameter takes effect only when the DestinationResource request parameter is set to SystemDisk.
        self.min = min
        # The state of the resource. Valid values:
        # 
        # *   Available
        # *   SoldOut
        self.status = status
        # The category of the resource based on stock status. Valid values:
        # 
        # *   WithStock: resources that are in sufficient stock
        # *   ClosedWithStock: resources that are in insufficient stock
        # *   WithoutStock: resources that are out of stock
        self.status_category = status_category
        # The unit of the disk capacity. This parameter takes effect only when the DestinationResource request parameter is set to SystemDisk.
        self.unit = unit
        # The resource type.
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

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResources(DaraModel):
    def __init__(
        self,
        condition_supported_resource: List[main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResource] = None,
    ):
        self.condition_supported_resource = condition_supported_resource

    def validate(self):
        if self.condition_supported_resource:
            for v1 in self.condition_supported_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionSupportedResource'] = []
        if self.condition_supported_resource is not None:
            for k1 in self.condition_supported_resource:
                result['ConditionSupportedResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_supported_resource = []
        if m.get('ConditionSupportedResource') is not None:
            for k1 in m.get('ConditionSupportedResource'):
                temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResource()
                self.condition_supported_resource.append(temp_model.from_map(k1))

        return self

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResource(DaraModel):
    def __init__(
        self,
        conditions: main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResourceConditions = None,
        max: int = None,
        min: int = None,
        status: str = None,
        status_category: str = None,
        unit: str = None,
        value: str = None,
    ):
        # The conditions.
        self.conditions = conditions
        # The maximum disk capacity.
        # 
        # This parameter takes effect only when the DestinationResource request parameter is set to SystemDisk.
        self.max = max
        # The minimum disk capacity.
        # 
        # This parameter takes effect only when the DestinationResource request parameter is set to SystemDisk.
        self.min = min
        # The stock state of the resource. Valid values:
        # 
        # *   Available
        # *   SoldOut
        self.status = status
        # The category of the resource based on stock status. Valid values:
        # 
        # *   WithStock: resources that are in sufficient stock
        # *   ClosedWithStock: resources that are in insufficient stock
        # *   WithoutStock: resources that are out of stock
        self.status_category = status_category
        # The unit of the disk capacity.
        # 
        # This parameter takes effect only when the DestinationResource request parameter is set to SystemDisk.
        self.unit = unit
        # The resource type.
        self.value = value

    def validate(self):
        if self.conditions:
            self.conditions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditions is not None:
            result['Conditions'] = self.conditions.to_map()

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
        if m.get('Conditions') is not None:
            temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResourceConditions()
            self.conditions = temp_model.from_map(m.get('Conditions'))

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

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResourceConditions(DaraModel):
    def __init__(
        self,
        condition: List[main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResourceConditionsCondition] = None,
    ):
        self.condition = condition

    def validate(self):
        if self.condition:
            for v1 in self.condition:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Condition'] = []
        if self.condition is not None:
            for k1 in self.condition:
                result['Condition'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition = []
        if m.get('Condition') is not None:
            for k1 in m.get('Condition'):
                temp_model = main_models.DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResourceConditionsCondition()
                self.condition.append(temp_model.from_map(k1))

        return self

class DescribeResourcesModificationResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceConditionSupportedResourcesConditionSupportedResourceConditionsCondition(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        # The condition name. Valid value:
        # 
        # DiskCategory, which indicates a disk category change.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

