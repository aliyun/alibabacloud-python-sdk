# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeEipAddressesResponseBody(DaraModel):
    def __init__(
        self,
        eip_addresses: main_models.DescribeEipAddressesResponseBodyEipAddresses = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.eip_addresses = eip_addresses
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()

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
        if m.get('EipAddresses') is not None:
            temp_model = main_models.DescribeEipAddressesResponseBodyEipAddresses()
            self.eip_addresses = temp_model.from_map(m.get('EipAddresses'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEipAddressesResponseBodyEipAddresses(DaraModel):
    def __init__(
        self,
        eip_address: List[main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddress] = None,
    ):
        self.eip_address = eip_address

    def validate(self):
        if self.eip_address:
            for v1 in self.eip_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k1 in self.eip_address:
                result['EipAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_address = []
        if m.get('EipAddress') is not None:
            for k1 in m.get('EipAddress'):
                temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k1))

        return self

class DescribeEipAddressesResponseBodyEipAddressesEipAddress(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        allocation_time: str = None,
        bandwidth: str = None,
        charge_type: str = None,
        eip_bandwidth: str = None,
        expired_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        operation_locks: main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocks = None,
        region_id: str = None,
        status: str = None,
    ):
        self.allocation_id = allocation_id
        self.allocation_time = allocation_time
        self.bandwidth = bandwidth
        self.charge_type = charge_type
        self.eip_bandwidth = eip_bandwidth
        self.expired_time = expired_time
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.ip_address = ip_address
        self.operation_locks = operation_locks
        self.region_id = region_id
        self.status = status

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.allocation_time is not None:
            result['AllocationTime'] = self.allocation_time

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('AllocationTime') is not None:
            self.allocation_time = m.get('AllocationTime')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: List[main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for v1 in self.lock_reason:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k1 in self.lock_reason:
                result['LockReason'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k1 in m.get('LockReason'):
                temp_model = main_models.DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k1))

        return self

class DescribeEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLockReason(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

