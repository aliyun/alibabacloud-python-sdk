# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedHostClustersResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_host_clusters: main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClusters = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array consisting of host group information.
        self.dedicated_host_clusters = dedicated_host_clusters
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of dedicated host clusters.
        self.total_count = total_count

    def validate(self):
        if self.dedicated_host_clusters:
            self.dedicated_host_clusters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_clusters is not None:
            result['DedicatedHostClusters'] = self.dedicated_host_clusters.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostClusters') is not None:
            temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClusters()
            self.dedicated_host_clusters = temp_model.from_map(m.get('DedicatedHostClusters'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClusters(DaraModel):
    def __init__(
        self,
        dedicated_host_cluster: List[main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostCluster] = None,
    ):
        self.dedicated_host_cluster = dedicated_host_cluster

    def validate(self):
        if self.dedicated_host_cluster:
            for v1 in self.dedicated_host_cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DedicatedHostCluster'] = []
        if self.dedicated_host_cluster is not None:
            for k1 in self.dedicated_host_cluster:
                result['DedicatedHostCluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_host_cluster = []
        if m.get('DedicatedHostCluster') is not None:
            for k1 in m.get('DedicatedHostCluster'):
                temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostCluster()
                self.dedicated_host_cluster.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostCluster(DaraModel):
    def __init__(
        self,
        dedicated_host_cluster_capacity: main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacity = None,
        dedicated_host_cluster_id: str = None,
        dedicated_host_cluster_name: str = None,
        dedicated_host_ids: main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostIds = None,
        description: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterTags = None,
        zone_id: str = None,
    ):
        # The capacity of the host group.
        self.dedicated_host_cluster_capacity = dedicated_host_cluster_capacity
        # The ID of the host group.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The name of the host group.
        self.dedicated_host_cluster_name = dedicated_host_cluster_name
        # The IDs of dedicated hosts in the host group.
        self.dedicated_host_ids = dedicated_host_ids
        # The description of the host group.
        self.description = description
        # The region ID of the host group.
        self.region_id = region_id
        # The resource group ID of the host group.
        self.resource_group_id = resource_group_id
        # The tags of the host group.
        self.tags = tags
        # The zone ID of the host group.
        self.zone_id = zone_id

    def validate(self):
        if self.dedicated_host_cluster_capacity:
            self.dedicated_host_cluster_capacity.validate()
        if self.dedicated_host_ids:
            self.dedicated_host_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_cluster_capacity is not None:
            result['DedicatedHostClusterCapacity'] = self.dedicated_host_cluster_capacity.to_map()

        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_cluster_name is not None:
            result['DedicatedHostClusterName'] = self.dedicated_host_cluster_name

        if self.dedicated_host_ids is not None:
            result['DedicatedHostIds'] = self.dedicated_host_ids.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostClusterCapacity') is not None:
            temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacity()
            self.dedicated_host_cluster_capacity = temp_model.from_map(m.get('DedicatedHostClusterCapacity'))

        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostClusterName') is not None:
            self.dedicated_host_cluster_name = m.get('DedicatedHostClusterName')

        if m.get('DedicatedHostIds') is not None:
            temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostIds()
            self.dedicated_host_ids = temp_model.from_map(m.get('DedicatedHostIds'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostIds(DaraModel):
    def __init__(
        self,
        dedicated_host_id: List[str] = None,
    ):
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacity(DaraModel):
    def __init__(
        self,
        available_instance_types: main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityAvailableInstanceTypes = None,
        available_memory: int = None,
        available_vcpus: int = None,
        local_storage_capacities: main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityLocalStorageCapacities = None,
        total_memory: int = None,
        total_vcpus: int = None,
    ):
        # The available capacity of ECS instances in the host group.
        self.available_instance_types = available_instance_types
        # The size of available memory. Unit: GiB
        self.available_memory = available_memory
        # The number of available vCPUs.
        self.available_vcpus = available_vcpus
        # The local storage capacity.
        self.local_storage_capacities = local_storage_capacities
        # The total memory size. Unit: GiB
        self.total_memory = total_memory
        # The total number of vCPUs.
        self.total_vcpus = total_vcpus

    def validate(self):
        if self.available_instance_types:
            self.available_instance_types.validate()
        if self.local_storage_capacities:
            self.local_storage_capacities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_instance_types is not None:
            result['AvailableInstanceTypes'] = self.available_instance_types.to_map()

        if self.available_memory is not None:
            result['AvailableMemory'] = self.available_memory

        if self.available_vcpus is not None:
            result['AvailableVcpus'] = self.available_vcpus

        if self.local_storage_capacities is not None:
            result['LocalStorageCapacities'] = self.local_storage_capacities.to_map()

        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory

        if self.total_vcpus is not None:
            result['TotalVcpus'] = self.total_vcpus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableInstanceTypes') is not None:
            temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityAvailableInstanceTypes()
            self.available_instance_types = temp_model.from_map(m.get('AvailableInstanceTypes'))

        if m.get('AvailableMemory') is not None:
            self.available_memory = m.get('AvailableMemory')

        if m.get('AvailableVcpus') is not None:
            self.available_vcpus = m.get('AvailableVcpus')

        if m.get('LocalStorageCapacities') is not None:
            temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityLocalStorageCapacities()
            self.local_storage_capacities = temp_model.from_map(m.get('LocalStorageCapacities'))

        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')

        if m.get('TotalVcpus') is not None:
            self.total_vcpus = m.get('TotalVcpus')

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityLocalStorageCapacities(DaraModel):
    def __init__(
        self,
        local_storage_capacity: List[main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityLocalStorageCapacitiesLocalStorageCapacity] = None,
    ):
        self.local_storage_capacity = local_storage_capacity

    def validate(self):
        if self.local_storage_capacity:
            for v1 in self.local_storage_capacity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LocalStorageCapacity'] = []
        if self.local_storage_capacity is not None:
            for k1 in self.local_storage_capacity:
                result['LocalStorageCapacity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.local_storage_capacity = []
        if m.get('LocalStorageCapacity') is not None:
            for k1 in m.get('LocalStorageCapacity'):
                temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityLocalStorageCapacitiesLocalStorageCapacity()
                self.local_storage_capacity.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityLocalStorageCapacitiesLocalStorageCapacity(DaraModel):
    def __init__(
        self,
        available_disk: int = None,
        data_disk_category: str = None,
        total_disk: int = None,
    ):
        # The available capacity of the local disk. Unit: GiB
        self.available_disk = available_disk
        # The category of data disks. Valid values:
        # 
        # *   cloud: basic disk
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   ephemeral_ssd: local SSD
        # *   cloud_essd: Enterprise SSD (ESSD)
        self.data_disk_category = data_disk_category
        # The total capacity of the local disk. Unit: GiB
        self.total_disk = total_disk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_disk is not None:
            result['AvailableDisk'] = self.available_disk

        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.total_disk is not None:
            result['TotalDisk'] = self.total_disk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableDisk') is not None:
            self.available_disk = m.get('AvailableDisk')

        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('TotalDisk') is not None:
            self.total_disk = m.get('TotalDisk')

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityAvailableInstanceTypes(DaraModel):
    def __init__(
        self,
        available_instance_type: List[main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityAvailableInstanceTypesAvailableInstanceType] = None,
    ):
        self.available_instance_type = available_instance_type

    def validate(self):
        if self.available_instance_type:
            for v1 in self.available_instance_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableInstanceType'] = []
        if self.available_instance_type is not None:
            for k1 in self.available_instance_type:
                result['AvailableInstanceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_instance_type = []
        if m.get('AvailableInstanceType') is not None:
            for k1 in m.get('AvailableInstanceType'):
                temp_model = main_models.DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityAvailableInstanceTypesAvailableInstanceType()
                self.available_instance_type.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostClustersResponseBodyDedicatedHostClustersDedicatedHostClusterDedicatedHostClusterCapacityAvailableInstanceTypesAvailableInstanceType(DaraModel):
    def __init__(
        self,
        available_instance_capacity: int = None,
        instance_type: str = None,
    ):
        # The available capacity of the ECS instance type.
        self.available_instance_capacity = available_instance_capacity
        # The ECS instance type.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_instance_capacity is not None:
            result['AvailableInstanceCapacity'] = self.available_instance_capacity

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableInstanceCapacity') is not None:
            self.available_instance_capacity = m.get('AvailableInstanceCapacity')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

