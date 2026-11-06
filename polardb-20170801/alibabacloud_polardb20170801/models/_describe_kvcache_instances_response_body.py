# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeKVCacheInstancesResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeKVCacheInstancesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        # The current page number.
        self.page_number = page_number
        # The number of instances returned on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of instances that match the filter conditions.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeKVCacheInstancesResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeKVCacheInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        kvcache_item: List[main_models.DescribeKVCacheInstancesResponseBodyItemsKVCacheItem] = None,
    ):
        self.kvcache_item = kvcache_item

    def validate(self):
        if self.kvcache_item:
            for v1 in self.kvcache_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KVCacheItem'] = []
        if self.kvcache_item is not None:
            for k1 in self.kvcache_item:
                result['KVCacheItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kvcache_item = []
        if m.get('KVCacheItem') is not None:
            for k1 in m.get('KVCacheItem'):
                temp_model = main_models.DescribeKVCacheInstancesResponseBodyItemsKVCacheItem()
                self.kvcache_item.append(temp_model.from_map(k1))

        return self

class DescribeKVCacheInstancesResponseBodyItemsKVCacheItem(DaraModel):
    def __init__(
        self,
        aidbcluster_id: str = None,
        creation_time: str = None,
        dbcluster_id: str = None,
        expire_time: str = None,
        expired: str = None,
        kvcache_instance_id: str = None,
        kvcache_instance_status: str = None,
        kvcache_space: int = None,
        pay_type: str = None,
        region_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.aidbcluster_id = aidbcluster_id
        self.creation_time = creation_time
        self.dbcluster_id = dbcluster_id
        self.expire_time = expire_time
        self.expired = expired
        self.kvcache_instance_id = kvcache_instance_id
        self.kvcache_instance_status = kvcache_instance_status
        self.kvcache_space = kvcache_space
        self.pay_type = pay_type
        self.region_id = region_id
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aidbcluster_id is not None:
            result['AIDBClusterId'] = self.aidbcluster_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.kvcache_instance_id is not None:
            result['KVCacheInstanceId'] = self.kvcache_instance_id

        if self.kvcache_instance_status is not None:
            result['KVCacheInstanceStatus'] = self.kvcache_instance_status

        if self.kvcache_space is not None:
            result['KVCacheSpace'] = self.kvcache_space

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIDBClusterId') is not None:
            self.aidbcluster_id = m.get('AIDBClusterId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('KVCacheInstanceId') is not None:
            self.kvcache_instance_id = m.get('KVCacheInstanceId')

        if m.get('KVCacheInstanceStatus') is not None:
            self.kvcache_instance_status = m.get('KVCacheInstanceStatus')

        if m.get('KVCacheSpace') is not None:
            self.kvcache_space = m.get('KVCacheSpace')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

