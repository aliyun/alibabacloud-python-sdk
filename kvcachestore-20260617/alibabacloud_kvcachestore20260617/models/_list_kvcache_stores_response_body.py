# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kvcachestore20260617 import models as main_models
from darabonba.model import DaraModel

class ListKVCacheStoresResponseBody(DaraModel):
    def __init__(
        self,
        kvcache_stores: List[main_models.ListKVCacheStoresResponseBodyKVCacheStores] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        page_total: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of KVCacheStore instances. Each element contains the following fields: KvcsId, Name, Status, ExtraStatus, RegionId, ZoneId, HpnZone, Type, Capacity, PaymentType, MountPointId, CreateTime, and Description.
        self.kvcache_stores = kvcache_stores
        # The maximum number of entries returned per pagination request.
        self.max_results = max_results
        # The pagination token for the next page. This value is empty when no more data is available. This parameter is valid only for cursor-based pagination.
        self.next_token = next_token
        # The current page number. This parameter is valid only for page number-based pagination.
        self.page_number = page_number
        # The number of entries per page. This parameter is valid only for page number-based pagination.
        self.page_size = page_size
        # The total number of pages. This value is returned only for page number-based pagination.
        self.page_total = page_total
        # The request ID. A request ID is returned regardless of whether the API call succeeds.
        self.request_id = request_id
        # The total number of instances. This value is returned only for page number-based pagination. For cursor-based pagination, the value is -1.
        self.total_count = total_count

    def validate(self):
        if self.kvcache_stores:
            for v1 in self.kvcache_stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KVCacheStores'] = []
        if self.kvcache_stores is not None:
            for k1 in self.kvcache_stores:
                result['KVCacheStores'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.page_total is not None:
            result['PageTotal'] = self.page_total

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kvcache_stores = []
        if m.get('KVCacheStores') is not None:
            for k1 in m.get('KVCacheStores'):
                temp_model = main_models.ListKVCacheStoresResponseBodyKVCacheStores()
                self.kvcache_stores.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListKVCacheStoresResponseBodyKVCacheStores(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        create_time: str = None,
        description: str = None,
        extra_status: str = None,
        hpn_zone: str = None,
        kvcs_id: str = None,
        mount_point_id: str = None,
        name: str = None,
        payment_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListKVCacheStoresResponseBodyKVCacheStoresTags] = None,
        type: str = None,
        zone_id: str = None,
    ):
        # The storage capacity. Unit: GiB.
        self.capacity = capacity
        # The creation time in ISO 8601 format.
        self.create_time = create_time
        # The instance description.
        self.description = description
        # The extra status information. Valid values: CapacityExpanding, CapacityExpandSuccess, and CapacityExpandFail.
        self.extra_status = extra_status
        # The cluster ID.
        self.hpn_zone = hpn_zone
        # The instance ID.
        self.kvcs_id = kvcs_id
        # The file system-level mount point ID. Instances under the same file system share this mount point. For more information, call ListKVCacheInstanceAttachInfo.
        self.mount_point_id = mount_point_id
        # The instance name.
        self.name = name
        # The payment type. Valid values: PREPAY and POSTPAY.
        self.payment_type = payment_type
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The instance status. Valid values: Creating, Available, InUse, Stopping, Stopped, and Deleting.
        self.status = status
        # The list of resource tags.
        self.tags = tags
        # The instance type. Valid values: kvcs (KVCacheStore, CPFS).
        self.type = type
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.extra_status is not None:
            result['ExtraStatus'] = self.extra_status

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.kvcs_id is not None:
            result['KvcsId'] = self.kvcs_id

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

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
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExtraStatus') is not None:
            self.extra_status = m.get('ExtraStatus')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('KvcsId') is not None:
            self.kvcs_id = m.get('KvcsId')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListKVCacheStoresResponseBodyKVCacheStoresTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListKVCacheStoresResponseBodyKVCacheStoresTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the resource.
        self.tag_key = tag_key
        # The tag value of the resource.
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

