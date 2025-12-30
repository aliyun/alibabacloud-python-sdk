# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmRecoveryPlanAvailableConfigResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstances = None,
        request_id: str = None,
    ):
        # The instances.
        self.instances = instances
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstance(DaraModel):
    def __init__(
        self,
        addr_pools: main_models.DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstanceAddrPools = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        # The address pools.
        self.addr_pools = addr_pools
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPools') is not None:
            temp_model = main_models.DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstanceAddrPools()
            self.addr_pools = temp_model.from_map(m.get('AddrPools'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

class DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstanceAddrPools(DaraModel):
    def __init__(
        self,
        addr_pool: List[main_models.DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstanceAddrPoolsAddrPool] = None,
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
                temp_model = main_models.DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstanceAddrPoolsAddrPool()
                self.addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeGtmRecoveryPlanAvailableConfigResponseBodyInstancesInstanceAddrPoolsAddrPool(DaraModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        name: str = None,
    ):
        # The address pool ID.
        self.addr_pool_id = addr_pool_id
        # The name of the address pool.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

