# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmRecoveryPlanResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        fault_addr_pool_num: int = None,
        fault_addr_pools: main_models.DescribeGtmRecoveryPlanResponseBodyFaultAddrPools = None,
        last_execute_time: str = None,
        last_execute_timestamp: int = None,
        last_rollback_time: str = None,
        last_rollback_timestamp: int = None,
        name: str = None,
        recovery_plan_id: int = None,
        remark: str = None,
        request_id: str = None,
        status: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the disaster recovery plan was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the disaster recovery plan was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The number of faulty address pools.
        self.fault_addr_pool_num = fault_addr_pool_num
        # The faulty address pools.
        self.fault_addr_pools = fault_addr_pools
        # The time when the disaster recovery plan was last executed. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.last_execute_time = last_execute_time
        # The time when the disaster recovery plan was last executed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_execute_timestamp = last_execute_timestamp
        # The time when the disaster recovery plan was last rolled back. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_rollback_time = last_rollback_time
        # The time when the disaster recovery plan was last rolled back. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_rollback_timestamp = last_rollback_timestamp
        # The name of the disaster recovery plan.
        self.name = name
        # The ID of the disaster recovery plan.
        self.recovery_plan_id = recovery_plan_id
        # The description of the disaster recovery plan.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The status of the disaster recovery plan.
        self.status = status
        # The time when the disaster recovery plan was last modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the disaster recovery plan was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.fault_addr_pools:
            self.fault_addr_pools.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.fault_addr_pool_num is not None:
            result['FaultAddrPoolNum'] = self.fault_addr_pool_num

        if self.fault_addr_pools is not None:
            result['FaultAddrPools'] = self.fault_addr_pools.to_map()

        if self.last_execute_time is not None:
            result['LastExecuteTime'] = self.last_execute_time

        if self.last_execute_timestamp is not None:
            result['LastExecuteTimestamp'] = self.last_execute_timestamp

        if self.last_rollback_time is not None:
            result['LastRollbackTime'] = self.last_rollback_time

        if self.last_rollback_timestamp is not None:
            result['LastRollbackTimestamp'] = self.last_rollback_timestamp

        if self.name is not None:
            result['Name'] = self.name

        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('FaultAddrPoolNum') is not None:
            self.fault_addr_pool_num = m.get('FaultAddrPoolNum')

        if m.get('FaultAddrPools') is not None:
            temp_model = main_models.DescribeGtmRecoveryPlanResponseBodyFaultAddrPools()
            self.fault_addr_pools = temp_model.from_map(m.get('FaultAddrPools'))

        if m.get('LastExecuteTime') is not None:
            self.last_execute_time = m.get('LastExecuteTime')

        if m.get('LastExecuteTimestamp') is not None:
            self.last_execute_timestamp = m.get('LastExecuteTimestamp')

        if m.get('LastRollbackTime') is not None:
            self.last_rollback_time = m.get('LastRollbackTime')

        if m.get('LastRollbackTimestamp') is not None:
            self.last_rollback_timestamp = m.get('LastRollbackTimestamp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeGtmRecoveryPlanResponseBodyFaultAddrPools(DaraModel):
    def __init__(
        self,
        fault_addr_pool: List[main_models.DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPool] = None,
    ):
        self.fault_addr_pool = fault_addr_pool

    def validate(self):
        if self.fault_addr_pool:
            for v1 in self.fault_addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FaultAddrPool'] = []
        if self.fault_addr_pool is not None:
            for k1 in self.fault_addr_pool:
                result['FaultAddrPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fault_addr_pool = []
        if m.get('FaultAddrPool') is not None:
            for k1 in m.get('FaultAddrPool'):
                temp_model = main_models.DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPool()
                self.fault_addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPool(DaraModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        addr_pool_name: str = None,
        addrs: main_models.DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPoolAddrs = None,
        instance_id: str = None,
    ):
        # The address pool ID.
        self.addr_pool_id = addr_pool_id
        # The address pool name.
        self.addr_pool_name = addr_pool_name
        self.addrs = addrs
        # The instance ID.
        self.instance_id = instance_id

    def validate(self):
        if self.addrs:
            self.addrs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id

        if self.addr_pool_name is not None:
            result['AddrPoolName'] = self.addr_pool_name

        if self.addrs is not None:
            result['Addrs'] = self.addrs.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')

        if m.get('AddrPoolName') is not None:
            self.addr_pool_name = m.get('AddrPoolName')

        if m.get('Addrs') is not None:
            temp_model = main_models.DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPoolAddrs()
            self.addrs = temp_model.from_map(m.get('Addrs'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPoolAddrs(DaraModel):
    def __init__(
        self,
        addr: List[main_models.DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPoolAddrsAddr] = None,
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
                temp_model = main_models.DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPoolAddrsAddr()
                self.addr.append(temp_model.from_map(k1))

        return self

class DescribeGtmRecoveryPlanResponseBodyFaultAddrPoolsFaultAddrPoolAddrsAddr(DaraModel):
    def __init__(
        self,
        id: int = None,
        mode: str = None,
        value: str = None,
    ):
        # The address ID.
        self.id = id
        # The address mode.
        self.mode = mode
        # The address.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

