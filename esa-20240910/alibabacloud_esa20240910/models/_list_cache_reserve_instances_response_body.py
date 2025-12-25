# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListCacheReserveInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_info: List[main_models.ListCacheReserveInstancesResponseBodyInstanceInfo] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The cache reserve instances.
        self.instance_info = instance_info
        # Page number. Default value: **1**.
        self.page_number = page_number
        # Page size, default **500**, range: **1~500**.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Total count.
        self.total_count = total_count
        # Total pages.
        self.total_page = total_page

    def validate(self):
        if self.instance_info:
            for v1 in self.instance_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k1 in self.instance_info:
                result['InstanceInfo'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k1 in m.get('InstanceInfo'):
                temp_model = main_models.ListCacheReserveInstancesResponseBodyInstanceInfo()
                self.instance_info.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListCacheReserveInstancesResponseBodyInstanceInfo(DaraModel):
    def __init__(
        self,
        cache_reserve_capacity: int = None,
        cache_reserve_region: str = None,
        charge_type: str = None,
        create_time: str = None,
        duration: int = None,
        expire_time: str = None,
        instance_id: str = None,
        status: str = None,
    ):
        # Cache reserve capacity. Unit: GB.
        self.cache_reserve_capacity = cache_reserve_capacity
        # Cache reserve usage region.
        self.cache_reserve_region = cache_reserve_region
        self.charge_type = charge_type
        # Instance purchase time.
        self.create_time = create_time
        # Duration of the instance purchase, unit: months.
        self.duration = duration
        # Instance expiration time.
        self.expire_time = expire_time
        # Instance ID.
        self.instance_id = instance_id
        # The status of the cache reserve instance. Valid values:
        # 
        # *   **online**: The instance is in service.
        # *   **offline**: The instance has expired within an allowable period. In this state, it is unavailable.
        # *   **disable**: The instance has been released.
        # *   **overdue**: The instance has been stopped due to overdue payments.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_reserve_capacity is not None:
            result['CacheReserveCapacity'] = self.cache_reserve_capacity

        if self.cache_reserve_region is not None:
            result['CacheReserveRegion'] = self.cache_reserve_region

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheReserveCapacity') is not None:
            self.cache_reserve_capacity = m.get('CacheReserveCapacity')

        if m.get('CacheReserveRegion') is not None:
            self.cache_reserve_region = m.get('CacheReserveRegion')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

