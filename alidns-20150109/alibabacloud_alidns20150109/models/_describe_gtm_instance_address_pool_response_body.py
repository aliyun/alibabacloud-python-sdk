# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmInstanceAddressPoolResponseBody(DaraModel):
    def __init__(
        self,
        addr_count: int = None,
        addr_pool_id: str = None,
        addrs: main_models.DescribeGtmInstanceAddressPoolResponseBodyAddrs = None,
        create_time: str = None,
        create_timestamp: int = None,
        min_available_addr_num: int = None,
        monitor_config_id: str = None,
        monitor_status: str = None,
        name: str = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The number of addresses in the address pool queried.
        self.addr_count = addr_count
        # The ID of the address pool.
        self.addr_pool_id = addr_pool_id
        # The addresses in the address pool.
        self.addrs = addrs
        # The time when the address pool was created.
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        # The minimum number of available addresses in the address pool.
        self.min_available_addr_num = min_available_addr_num
        # The health check ID of the address pool.
        self.monitor_config_id = monitor_config_id
        # Indicates whether health check was enabled for the address pool. Valid values:
        # 
        # *   **OPEN**: Enabled
        # *   **CLOSE**: Disabled
        # *   **UNCONFIGURED**: Not configured
        self.monitor_status = monitor_status
        # The name of the address pool.
        self.name = name
        # The ID of the request.
        self.request_id = request_id
        # The availability status of the address pool. Valid values:
        # 
        # *   **AVAILABLE**: Available
        # *   **NOT_AVAILABLE**: Unavailable
        self.status = status
        # The type of the address pool. Valid values:
        # 
        # *   **IP**: IP address
        # *   **DOMAIN**: Domain name
        self.type = type
        # The last time when the address pool was updated.
        self.update_time = update_time
        # A timestamp that indicates the last time the address pool was updated.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.addrs:
            self.addrs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count

        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id

        if self.addrs is not None:
            result['Addrs'] = self.addrs.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.min_available_addr_num is not None:
            result['MinAvailableAddrNum'] = self.min_available_addr_num

        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id

        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Addrs') is not None:
            temp_model = main_models.DescribeGtmInstanceAddressPoolResponseBodyAddrs()
            self.addrs = temp_model.from_map(m.get('Addrs'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('MinAvailableAddrNum') is not None:
            self.min_available_addr_num = m.get('MinAvailableAddrNum')

        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')

        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeGtmInstanceAddressPoolResponseBodyAddrs(DaraModel):
    def __init__(
        self,
        addr: List[main_models.DescribeGtmInstanceAddressPoolResponseBodyAddrsAddr] = None,
    ):
        self.addr = addr

    def validate(self):
        if self.addr:
            for v1 in self.addr:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addr'] = []
        if self.addr is not None:
            for k1 in self.addr:
                result['Addr'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k1 in m.get('Addr'):
                temp_model = main_models.DescribeGtmInstanceAddressPoolResponseBodyAddrsAddr()
                self.addr.append(temp_model.from_map(k1))

        return self

class DescribeGtmInstanceAddressPoolResponseBodyAddrsAddr(DaraModel):
    def __init__(
        self,
        addr_id: int = None,
        alert_status: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        lba_weight: int = None,
        mode: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        value: str = None,
    ):
        # The ID of the address.
        self.addr_id = addr_id
        # Indicates whether health check was enabled for the address. Valid values:
        # 
        # *   **OK**: Normal
        # *   **ALERT**: Alert
        self.alert_status = alert_status
        # The time when the address pool was created.
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        # The weight of the address.
        self.lba_weight = lba_weight
        # The mode of the address. Valid values:
        # 
        # *   **SMART**: Intelligent return
        # *   **ONLINE**: Always online
        # *   **OFFLINE**: Always offline
        self.mode = mode
        # The last time when the address was updated.
        self.update_time = update_time
        # A timestamp that indicates the last time when the address was updated.
        self.update_timestamp = update_timestamp
        # The address.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_id is not None:
            result['AddrId'] = self.addr_id

        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrId') is not None:
            self.addr_id = m.get('AddrId')

        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

