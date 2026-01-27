# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedBlockStorageClustersResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_block_storage_clusters: List[main_models.DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClusters] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the dedicated block storage clusters.
        self.dedicated_block_storage_clusters = dedicated_block_storage_clusters
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dedicated_block_storage_clusters:
            for v1 in self.dedicated_block_storage_clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DedicatedBlockStorageClusters'] = []
        if self.dedicated_block_storage_clusters is not None:
            for k1 in self.dedicated_block_storage_clusters:
                result['DedicatedBlockStorageClusters'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        self.dedicated_block_storage_clusters = []
        if m.get('DedicatedBlockStorageClusters') is not None:
            for k1 in m.get('DedicatedBlockStorageClusters'):
                temp_model = main_models.DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClusters()
                self.dedicated_block_storage_clusters.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClusters(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        category: str = None,
        create_time: str = None,
        dedicated_block_storage_cluster_capacity: main_models.DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity = None,
        dedicated_block_storage_cluster_id: str = None,
        dedicated_block_storage_cluster_name: str = None,
        description: str = None,
        enable_thin_provision: bool = None,
        expired_time: str = None,
        performance_level: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        size_over_sold_ratio: float = None,
        status: str = None,
        storage_domain: str = None,
        supported_category: str = None,
        tags: List[main_models.DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags] = None,
        type: str = None,
        zone_id: str = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
        # The category of disks that can be created in the dedicated block storage cluster.
        self.category = category
        # The time when the dedicated block storage cluster was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # Details about the storage capacity of the dedicated block storage cluster.
        self.dedicated_block_storage_cluster_capacity = dedicated_block_storage_cluster_capacity
        # The ID of the dedicated block storage cluster.
        self.dedicated_block_storage_cluster_id = dedicated_block_storage_cluster_id
        # The name of the dedicated block storage cluster.
        self.dedicated_block_storage_cluster_name = dedicated_block_storage_cluster_name
        # The description of the dedicated block storage cluster.
        self.description = description
        # Indicates whether Thin Provision is enabled.
        self.enable_thin_provision = enable_thin_provision
        # The time when the dedicated block storage cluster expires. The value is a UNIX timestamp. Unit: seconds.
        self.expired_time = expired_time
        # The performance level of disks. Valid values:
        # 
        # *   PL0
        # *   PL1
        # *   PL2
        # *   PL3
        # 
        # >  This parameter is valid only when the SupportedCategory value is cloud_essd.
        self.performance_level = performance_level
        # The region ID of the dedicated block storage cluster.
        self.region_id = region_id
        # The ID of the resource group to which the dedicated block storage cluster belongs. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to obtain the ID of the resource group.
        self.resource_group_id = resource_group_id
        # The capacity oversold ratio.
        self.size_over_sold_ratio = size_over_sold_ratio
        # The state of the dedicated block storage cluster. Valid values:
        # 
        # *   Preparing
        # *   Running
        # *   Expired
        # *   Offline
        self.status = status
        # StorageDomain
        self.storage_domain = storage_domain
        # This parameter is not supported.
        self.supported_category = supported_category
        # The tags of the dedicated block storage cluster.
        self.tags = tags
        # The type of the dedicated block storage cluster. Valid values:
        # 
        # *   Standard: basic dedicated block storage cluster. ESSDs at performance level 0 (PL0 ESSDs) can be created in basic dedicated block storage clusters.
        # *   Premium: performance dedicated block storage cluster. ESSDs at performance level 1 (PL1 ESSDs) can be created in performance dedicated block storage clusters.
        self.type = type
        # The zone ID of the dedicated block storage cluster.
        self.zone_id = zone_id

    def validate(self):
        if self.dedicated_block_storage_cluster_capacity:
            self.dedicated_block_storage_cluster_capacity.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dedicated_block_storage_cluster_capacity is not None:
            result['DedicatedBlockStorageClusterCapacity'] = self.dedicated_block_storage_cluster_capacity.to_map()

        if self.dedicated_block_storage_cluster_id is not None:
            result['DedicatedBlockStorageClusterId'] = self.dedicated_block_storage_cluster_id

        if self.dedicated_block_storage_cluster_name is not None:
            result['DedicatedBlockStorageClusterName'] = self.dedicated_block_storage_cluster_name

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_thin_provision is not None:
            result['EnableThinProvision'] = self.enable_thin_provision

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.size_over_sold_ratio is not None:
            result['SizeOverSoldRatio'] = self.size_over_sold_ratio

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_domain is not None:
            result['StorageDomain'] = self.storage_domain

        if self.supported_category is not None:
            result['SupportedCategory'] = self.supported_category

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DedicatedBlockStorageClusterCapacity') is not None:
            temp_model = main_models.DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity()
            self.dedicated_block_storage_cluster_capacity = temp_model.from_map(m.get('DedicatedBlockStorageClusterCapacity'))

        if m.get('DedicatedBlockStorageClusterId') is not None:
            self.dedicated_block_storage_cluster_id = m.get('DedicatedBlockStorageClusterId')

        if m.get('DedicatedBlockStorageClusterName') is not None:
            self.dedicated_block_storage_cluster_name = m.get('DedicatedBlockStorageClusterName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableThinProvision') is not None:
            self.enable_thin_provision = m.get('EnableThinProvision')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SizeOverSoldRatio') is not None:
            self.size_over_sold_ratio = m.get('SizeOverSoldRatio')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageDomain') is not None:
            self.storage_domain = m.get('StorageDomain')

        if m.get('SupportedCategory') is not None:
            self.supported_category = m.get('SupportedCategory')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the dedicated block storage cluster.
        self.tag_key = tag_key
        # The tag value of the dedicated block storage cluster.
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

class DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity(DaraModel):
    def __init__(
        self,
        available_capacity: int = None,
        available_device_capacity: int = None,
        available_space_capacity: float = None,
        cluster_available_capacity: int = None,
        cluster_delivery_capacity: int = None,
        delivery_capacity: int = None,
        total_capacity: int = None,
        total_device_capacity: int = None,
        total_space_capacity: int = None,
        used_capacity: int = None,
        used_device_capacity: int = None,
        used_space_capacity: float = None,
    ):
        # The available capacity of the dedicated block storage cluster. Unit: GiB.
        self.available_capacity = available_capacity
        # The total capacity of the dedicated block storage cluster that was delivered in disk creation orders. Unit: GB.
        self.available_device_capacity = available_device_capacity
        # This parameter is displayed only if Thin Provision is enabled.
        self.available_space_capacity = available_space_capacity
        # The capacity of the dedicated block storage cluster that was delivered in orders. Unit: GB.
        self.cluster_available_capacity = cluster_available_capacity
        # The capacity of the dedicated block storage cluster that is to be delivered in orders. Unit: GB.
        self.cluster_delivery_capacity = cluster_delivery_capacity
        # The capacity to be delivered for the dedicated block storage cluster. Unit: GiB.
        self.delivery_capacity = delivery_capacity
        # The total capacity of the dedicated block storage cluster. Unit: GiB.
        self.total_capacity = total_capacity
        # The total capacity of the dedicated block storage cluster that is to be delivered in disk creation orders. Unit: GB.
        self.total_device_capacity = total_device_capacity
        # This parameter is displayed only if Thin Provision is enabled.
        self.total_space_capacity = total_space_capacity
        # The used capacity of the dedicated block storage cluster. Unit: GiB.
        self.used_capacity = used_capacity
        # The capacity of the dedicated block storage cluster that was used to create disks. Unit: GB.
        self.used_device_capacity = used_device_capacity
        # This parameter is displayed only if Thin Provision is enabled.
        self.used_space_capacity = used_space_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_capacity is not None:
            result['AvailableCapacity'] = self.available_capacity

        if self.available_device_capacity is not None:
            result['AvailableDeviceCapacity'] = self.available_device_capacity

        if self.available_space_capacity is not None:
            result['AvailableSpaceCapacity'] = self.available_space_capacity

        if self.cluster_available_capacity is not None:
            result['ClusterAvailableCapacity'] = self.cluster_available_capacity

        if self.cluster_delivery_capacity is not None:
            result['ClusterDeliveryCapacity'] = self.cluster_delivery_capacity

        if self.delivery_capacity is not None:
            result['DeliveryCapacity'] = self.delivery_capacity

        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.total_device_capacity is not None:
            result['TotalDeviceCapacity'] = self.total_device_capacity

        if self.total_space_capacity is not None:
            result['TotalSpaceCapacity'] = self.total_space_capacity

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        if self.used_device_capacity is not None:
            result['UsedDeviceCapacity'] = self.used_device_capacity

        if self.used_space_capacity is not None:
            result['UsedSpaceCapacity'] = self.used_space_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableCapacity') is not None:
            self.available_capacity = m.get('AvailableCapacity')

        if m.get('AvailableDeviceCapacity') is not None:
            self.available_device_capacity = m.get('AvailableDeviceCapacity')

        if m.get('AvailableSpaceCapacity') is not None:
            self.available_space_capacity = m.get('AvailableSpaceCapacity')

        if m.get('ClusterAvailableCapacity') is not None:
            self.cluster_available_capacity = m.get('ClusterAvailableCapacity')

        if m.get('ClusterDeliveryCapacity') is not None:
            self.cluster_delivery_capacity = m.get('ClusterDeliveryCapacity')

        if m.get('DeliveryCapacity') is not None:
            self.delivery_capacity = m.get('DeliveryCapacity')

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('TotalDeviceCapacity') is not None:
            self.total_device_capacity = m.get('TotalDeviceCapacity')

        if m.get('TotalSpaceCapacity') is not None:
            self.total_space_capacity = m.get('TotalSpaceCapacity')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        if m.get('UsedDeviceCapacity') is not None:
            self.used_device_capacity = m.get('UsedDeviceCapacity')

        if m.get('UsedSpaceCapacity') is not None:
            self.used_space_capacity = m.get('UsedSpaceCapacity')

        return self

