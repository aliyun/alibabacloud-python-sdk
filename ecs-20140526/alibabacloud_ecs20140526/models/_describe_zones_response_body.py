# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeZonesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zones: main_models.DescribeZonesResponseBodyZones = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Details about the zones and their supported resources.
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.zones is not None:
            result['Zones'] = self.zones.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Zones') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m.get('Zones'))

        return self

class DescribeZonesResponseBodyZones(DaraModel):
    def __init__(
        self,
        zone: List[main_models.DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for v1 in self.zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Zone'] = []
        if self.zone is not None:
            for k1 in self.zone:
                result['Zone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k1 in m.get('Zone'):
                temp_model = main_models.DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k1))

        return self

class DescribeZonesResponseBodyZonesZone(DaraModel):
    def __init__(
        self,
        available_dedicated_host_types: main_models.DescribeZonesResponseBodyZonesZoneAvailableDedicatedHostTypes = None,
        available_disk_categories: main_models.DescribeZonesResponseBodyZonesZoneAvailableDiskCategories = None,
        available_instance_types: main_models.DescribeZonesResponseBodyZonesZoneAvailableInstanceTypes = None,
        available_resource_creation: main_models.DescribeZonesResponseBodyZonesZoneAvailableResourceCreation = None,
        available_resources: main_models.DescribeZonesResponseBodyZonesZoneAvailableResources = None,
        available_volume_categories: main_models.DescribeZonesResponseBodyZonesZoneAvailableVolumeCategories = None,
        dedicated_host_generations: main_models.DescribeZonesResponseBodyZonesZoneDedicatedHostGenerations = None,
        local_name: str = None,
        zone_id: str = None,
        zone_type: str = None,
    ):
        # The supported dedicated host types.
        self.available_dedicated_host_types = available_dedicated_host_types
        # The categories of cloud disks that can be created. Valid values:
        # 
        # *   cloud: basic disk
        # *   cloud_ssd: standard SSD
        # *   cloud_efficiency: ultra disk
        # *   cloud_essd: ESSD
        self.available_disk_categories = available_disk_categories
        # The supported instance types.
        self.available_instance_types = available_instance_types
        # The types of resources that can be created. Valid values:
        # 
        # *   VSwitch: vSwitch
        # *   IoOptimized: I/O optimized instance
        # *   Instance: instance
        # *   DedicatedHost: dedicated host
        # *   disk: cloud disk
        self.available_resource_creation = available_resource_creation
        # Details about the resources that can be created in the zone.
        self.available_resources = available_resources
        # The supported Shared Block Storage device categories.
        self.available_volume_categories = available_volume_categories
        # The supported generations of dedicated hosts.
        self.dedicated_host_generations = dedicated_host_generations
        # The name of the zone in the local language.
        self.local_name = local_name
        # The ID of the zone.
        self.zone_id = zone_id
        # The type of the zone. Valid values:
        # 
        # *   AvailabilityZone: zone for the Alibaba Cloud public cloud
        # *   CloudBoxZone: zone for CloudBox
        self.zone_type = zone_type

    def validate(self):
        if self.available_dedicated_host_types:
            self.available_dedicated_host_types.validate()
        if self.available_disk_categories:
            self.available_disk_categories.validate()
        if self.available_instance_types:
            self.available_instance_types.validate()
        if self.available_resource_creation:
            self.available_resource_creation.validate()
        if self.available_resources:
            self.available_resources.validate()
        if self.available_volume_categories:
            self.available_volume_categories.validate()
        if self.dedicated_host_generations:
            self.dedicated_host_generations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_dedicated_host_types is not None:
            result['AvailableDedicatedHostTypes'] = self.available_dedicated_host_types.to_map()

        if self.available_disk_categories is not None:
            result['AvailableDiskCategories'] = self.available_disk_categories.to_map()

        if self.available_instance_types is not None:
            result['AvailableInstanceTypes'] = self.available_instance_types.to_map()

        if self.available_resource_creation is not None:
            result['AvailableResourceCreation'] = self.available_resource_creation.to_map()

        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()

        if self.available_volume_categories is not None:
            result['AvailableVolumeCategories'] = self.available_volume_categories.to_map()

        if self.dedicated_host_generations is not None:
            result['DedicatedHostGenerations'] = self.dedicated_host_generations.to_map()

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableDedicatedHostTypes') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableDedicatedHostTypes()
            self.available_dedicated_host_types = temp_model.from_map(m.get('AvailableDedicatedHostTypes'))

        if m.get('AvailableDiskCategories') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableDiskCategories()
            self.available_disk_categories = temp_model.from_map(m.get('AvailableDiskCategories'))

        if m.get('AvailableInstanceTypes') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableInstanceTypes()
            self.available_instance_types = temp_model.from_map(m.get('AvailableInstanceTypes'))

        if m.get('AvailableResourceCreation') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResourceCreation()
            self.available_resource_creation = temp_model.from_map(m.get('AvailableResourceCreation'))

        if m.get('AvailableResources') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResources()
            self.available_resources = temp_model.from_map(m.get('AvailableResources'))

        if m.get('AvailableVolumeCategories') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableVolumeCategories()
            self.available_volume_categories = temp_model.from_map(m.get('AvailableVolumeCategories'))

        if m.get('DedicatedHostGenerations') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneDedicatedHostGenerations()
            self.dedicated_host_generations = temp_model.from_map(m.get('DedicatedHostGenerations'))

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

class DescribeZonesResponseBodyZonesZoneDedicatedHostGenerations(DaraModel):
    def __init__(
        self,
        dedicated_host_generation: List[str] = None,
    ):
        self.dedicated_host_generation = dedicated_host_generation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_generation is not None:
            result['DedicatedHostGeneration'] = self.dedicated_host_generation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGeneration') is not None:
            self.dedicated_host_generation = m.get('DedicatedHostGeneration')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableVolumeCategories(DaraModel):
    def __init__(
        self,
        volume_categories: List[str] = None,
    ):
        self.volume_categories = volume_categories

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.volume_categories is not None:
            result['VolumeCategories'] = self.volume_categories

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VolumeCategories') is not None:
            self.volume_categories = m.get('VolumeCategories')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResources(DaraModel):
    def __init__(
        self,
        resources_info: List[main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfo] = None,
    ):
        self.resources_info = resources_info

    def validate(self):
        if self.resources_info:
            for v1 in self.resources_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourcesInfo'] = []
        if self.resources_info is not None:
            for k1 in self.resources_info:
                result['ResourcesInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resources_info = []
        if m.get('ResourcesInfo') is not None:
            for k1 in m.get('ResourcesInfo'):
                temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfo()
                self.resources_info.append(temp_model.from_map(k1))

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfo(DaraModel):
    def __init__(
        self,
        data_disk_categories: main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoDataDiskCategories = None,
        instance_generations: main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceGenerations = None,
        instance_type_families: main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypeFamilies = None,
        instance_types: main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypes = None,
        io_optimized: bool = None,
        network_types: main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoNetworkTypes = None,
        system_disk_categories: main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoSystemDiskCategories = None,
    ):
        # The categories of data disks that can be created.
        self.data_disk_categories = data_disk_categories
        # The supported generations of instance families.
        self.instance_generations = instance_generations
        # The supported instance families.
        self.instance_type_families = instance_type_families
        # The supported instance types.
        self.instance_types = instance_types
        # Indicates whether the instance is I/O optimized.
        self.io_optimized = io_optimized
        # The supported network types.
        self.network_types = network_types
        # The categories of system disks that can be created.
        self.system_disk_categories = system_disk_categories

    def validate(self):
        if self.data_disk_categories:
            self.data_disk_categories.validate()
        if self.instance_generations:
            self.instance_generations.validate()
        if self.instance_type_families:
            self.instance_type_families.validate()
        if self.instance_types:
            self.instance_types.validate()
        if self.network_types:
            self.network_types.validate()
        if self.system_disk_categories:
            self.system_disk_categories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_categories is not None:
            result['DataDiskCategories'] = self.data_disk_categories.to_map()

        if self.instance_generations is not None:
            result['InstanceGenerations'] = self.instance_generations.to_map()

        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families.to_map()

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.network_types is not None:
            result['NetworkTypes'] = self.network_types.to_map()

        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategories') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoDataDiskCategories()
            self.data_disk_categories = temp_model.from_map(m.get('DataDiskCategories'))

        if m.get('InstanceGenerations') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceGenerations()
            self.instance_generations = temp_model.from_map(m.get('InstanceGenerations'))

        if m.get('InstanceTypeFamilies') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypeFamilies()
            self.instance_type_families = temp_model.from_map(m.get('InstanceTypeFamilies'))

        if m.get('InstanceTypes') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypes()
            self.instance_types = temp_model.from_map(m.get('InstanceTypes'))

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('NetworkTypes') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoNetworkTypes()
            self.network_types = temp_model.from_map(m.get('NetworkTypes'))

        if m.get('SystemDiskCategories') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoSystemDiskCategories()
            self.system_disk_categories = temp_model.from_map(m.get('SystemDiskCategories'))

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoSystemDiskCategories(DaraModel):
    def __init__(
        self,
        supported_system_disk_category: List[str] = None,
    ):
        self.supported_system_disk_category = supported_system_disk_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_system_disk_category is not None:
            result['supportedSystemDiskCategory'] = self.supported_system_disk_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedSystemDiskCategory') is not None:
            self.supported_system_disk_category = m.get('supportedSystemDiskCategory')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoNetworkTypes(DaraModel):
    def __init__(
        self,
        supported_network_category: List[str] = None,
    ):
        self.supported_network_category = supported_network_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_network_category is not None:
            result['supportedNetworkCategory'] = self.supported_network_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedNetworkCategory') is not None:
            self.supported_network_category = m.get('supportedNetworkCategory')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypes(DaraModel):
    def __init__(
        self,
        supported_instance_type: List[str] = None,
    ):
        self.supported_instance_type = supported_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_instance_type is not None:
            result['supportedInstanceType'] = self.supported_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedInstanceType') is not None:
            self.supported_instance_type = m.get('supportedInstanceType')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypeFamilies(DaraModel):
    def __init__(
        self,
        supported_instance_type_family: List[str] = None,
    ):
        self.supported_instance_type_family = supported_instance_type_family

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_instance_type_family is not None:
            result['supportedInstanceTypeFamily'] = self.supported_instance_type_family

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedInstanceTypeFamily') is not None:
            self.supported_instance_type_family = m.get('supportedInstanceTypeFamily')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceGenerations(DaraModel):
    def __init__(
        self,
        supported_instance_generation: List[str] = None,
    ):
        self.supported_instance_generation = supported_instance_generation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_instance_generation is not None:
            result['supportedInstanceGeneration'] = self.supported_instance_generation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedInstanceGeneration') is not None:
            self.supported_instance_generation = m.get('supportedInstanceGeneration')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoDataDiskCategories(DaraModel):
    def __init__(
        self,
        supported_data_disk_category: List[str] = None,
    ):
        self.supported_data_disk_category = supported_data_disk_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_data_disk_category is not None:
            result['supportedDataDiskCategory'] = self.supported_data_disk_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedDataDiskCategory') is not None:
            self.supported_data_disk_category = m.get('supportedDataDiskCategory')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableResourceCreation(DaraModel):
    def __init__(
        self,
        resource_types: List[str] = None,
    ):
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableInstanceTypes(DaraModel):
    def __init__(
        self,
        instance_types: List[str] = None,
    ):
        self.instance_types = instance_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableDiskCategories(DaraModel):
    def __init__(
        self,
        disk_categories: List[str] = None,
    ):
        self.disk_categories = disk_categories

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_categories is not None:
            result['DiskCategories'] = self.disk_categories

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskCategories') is not None:
            self.disk_categories = m.get('DiskCategories')

        return self

class DescribeZonesResponseBodyZonesZoneAvailableDedicatedHostTypes(DaraModel):
    def __init__(
        self,
        dedicated_host_type: List[str] = None,
    ):
        self.dedicated_host_type = dedicated_host_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_type is not None:
            result['DedicatedHostType'] = self.dedicated_host_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostType') is not None:
            self.dedicated_host_type = m.get('DedicatedHostType')

        return self

