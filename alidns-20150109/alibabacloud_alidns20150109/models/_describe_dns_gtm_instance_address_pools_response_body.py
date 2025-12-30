# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsGtmInstanceAddressPoolsResponseBody(DaraModel):
    def __init__(
        self,
        addr_pools: main_models.DescribeDnsGtmInstanceAddressPoolsResponseBodyAddrPools = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The returned address pools.
        self.addr_pools = addr_pools
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned on all pages.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.addr_pools:
            self.addr_pools.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_pools is not None:
            result['AddrPools'] = self.addr_pools.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPools') is not None:
            temp_model = main_models.DescribeDnsGtmInstanceAddressPoolsResponseBodyAddrPools()
            self.addr_pools = temp_model.from_map(m.get('AddrPools'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeDnsGtmInstanceAddressPoolsResponseBodyAddrPools(DaraModel):
    def __init__(
        self,
        addr_pool: List[main_models.DescribeDnsGtmInstanceAddressPoolsResponseBodyAddrPoolsAddrPool] = None,
    ):
        self.addr_pool = addr_pool

    def validate(self):
        if self.addr_pool:
            for v1 in self.addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddrPool'] = []
        if self.addr_pool is not None:
            for k1 in self.addr_pool:
                result['AddrPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr_pool = []
        if m.get('AddrPool') is not None:
            for k1 in m.get('AddrPool'):
                temp_model = main_models.DescribeDnsGtmInstanceAddressPoolsResponseBodyAddrPoolsAddrPool()
                self.addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmInstanceAddressPoolsResponseBodyAddrPoolsAddrPool(DaraModel):
    def __init__(
        self,
        addr_count: int = None,
        addr_pool_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        lba_strategy: str = None,
        monitor_config_id: str = None,
        monitor_status: str = None,
        name: str = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The number of addresses in the address pool.
        self.addr_count = addr_count
        # The ID of the address pool.
        self.addr_pool_id = addr_pool_id
        # The time when the address pool was created.
        self.create_time = create_time
        # The timestamp that indicates when the address pool was created.
        self.create_timestamp = create_timestamp
        # The load balancing policy of the address pool. Valid values:
        # 
        # *   ALL_RR: returns all addresses.
        # *   RATIO: returns addresses by weight.
        self.lba_strategy = lba_strategy
        # The ID of the health check task.
        self.monitor_config_id = monitor_config_id
        # Indicates whether health checks are configured. Valid values:
        # 
        # *   OPEN: enabled
        # *   CLOSE: disabled
        # *   UNCONFIGURED: not configured
        self.monitor_status = monitor_status
        # The name of the address pool.
        self.name = name
        # The type of the address pool. Valid values:
        # 
        # *   IPV4: IPv4 address
        # *   IPV6: IPv6 address
        # *   DOMAIN: domain name
        self.type = type
        # The time when the address pool was updated.
        self.update_time = update_time
        # The timestamp that indicates when the address pool was updated.
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count

        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy

        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id

        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')

        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')

        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')

        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

