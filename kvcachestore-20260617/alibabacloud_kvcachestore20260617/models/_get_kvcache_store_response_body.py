# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kvcachestore20260617 import models as main_models
from darabonba.model import DaraModel

class GetKVCacheStoreResponseBody(DaraModel):
    def __init__(
        self,
        kv_cache_store: main_models.GetKVCacheStoreResponseBodyKvCacheStore = None,
        request_id: str = None,
    ):
        self.kv_cache_store = kv_cache_store
        self.request_id = request_id

    def validate(self):
        if self.kv_cache_store:
            self.kv_cache_store.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kv_cache_store is not None:
            result['KvCacheStore'] = self.kv_cache_store.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KvCacheStore') is not None:
            temp_model = main_models.GetKVCacheStoreResponseBodyKvCacheStore()
            self.kv_cache_store = temp_model.from_map(m.get('KvCacheStore'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetKVCacheStoreResponseBodyKvCacheStore(DaraModel):
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
        tags: List[main_models.GetKVCacheStoreResponseBodyKvCacheStoreTags] = None,
        type: str = None,
        zone_id: str = None,
    ):
        self.capacity = capacity
        self.create_time = create_time
        self.description = description
        self.extra_status = extra_status
        self.hpn_zone = hpn_zone
        self.kvcs_id = kvcs_id
        self.mount_point_id = mount_point_id
        self.name = name
        self.payment_type = payment_type
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.tags = tags
        self.type = type
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
                temp_model = main_models.GetKVCacheStoreResponseBodyKvCacheStoreTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetKVCacheStoreResponseBodyKvCacheStoreTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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

