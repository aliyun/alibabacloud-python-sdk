# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class AddDnsGtmAccessStrategyRequest(DaraModel):
    def __init__(
        self,
        default_addr_pool: List[main_models.AddDnsGtmAccessStrategyRequestDefaultAddrPool] = None,
        default_addr_pool_type: str = None,
        default_latency_optimization: str = None,
        default_lba_strategy: str = None,
        default_max_return_addr_num: int = None,
        default_min_available_addr_num: int = None,
        failover_addr_pool: List[main_models.AddDnsGtmAccessStrategyRequestFailoverAddrPool] = None,
        failover_addr_pool_type: str = None,
        failover_latency_optimization: str = None,
        failover_lba_strategy: str = None,
        failover_max_return_addr_num: int = None,
        failover_min_available_addr_num: int = None,
        instance_id: str = None,
        lang: str = None,
        lines: str = None,
        strategy_mode: str = None,
        strategy_name: str = None,
    ):
        # The collection of primary address pools.
        # 
        # This parameter is required.
        self.default_addr_pool = default_addr_pool
        # The type of the primary address pool.
        # 
        # - IPV4
        # 
        # - IPV6
        # 
        # - DOMAIN
        # 
        # This parameter is required.
        self.default_addr_pool_type = default_addr_pool_type
        # The latency-based scheduling optimization for the primary address pool collection.
        # 
        # - OPEN: enabled
        # 
        # - CLOSE: disabled
        self.default_latency_optimization = default_latency_optimization
        # The load balancing policy for the primary address pool collection.
        # 
        # - ALL_RR: returns all addresses.
        # 
        # - RATIO: returns addresses by weight.
        self.default_lba_strategy = default_lba_strategy
        # The maximum number of addresses returned from the primary address pool collection.
        self.default_max_return_addr_num = default_max_return_addr_num
        # The minimum number of active addresses in the primary address pool collection.
        # 
        # This parameter is required.
        self.default_min_available_addr_num = default_min_available_addr_num
        # The collection of failover address pools. If a failover address pool collection is not configured, enter "EMPTY".
        self.failover_addr_pool = failover_addr_pool
        # The type of the failover address pool.
        # 
        # - IPV4
        # 
        # - IPV6
        # 
        # - DOMAIN
        self.failover_addr_pool_type = failover_addr_pool_type
        # The latency-based scheduling optimization for the failover address pool collection.
        # 
        # - OPEN: enabled
        # 
        # - CLOSE: disabled
        self.failover_latency_optimization = failover_latency_optimization
        # The load balancing policy for the failover address pool collection.
        # 
        # - ALL_RR: returns all addresses.
        # 
        # - RATIO: returns addresses by weight.
        self.failover_lba_strategy = failover_lba_strategy
        # The maximum number of addresses returned from the failover address pool collection.
        self.failover_max_return_addr_num = failover_max_return_addr_num
        # The minimum number of active addresses in the failover address pool collection.
        self.failover_min_available_addr_num = failover_min_available_addr_num
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of some returned parameters. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The source of the DNS request. For example, `["default", "drpeng"]` indicates a global policy and Dr. Peng Group.
        self.lines = lines
        # The type of the access policy.
        # 
        # - GEO: a location-based access policy.
        # 
        # - LATENCY: a latency-based access policy.
        # 
        # This parameter is required.
        self.strategy_mode = strategy_mode
        # The policy name.
        # 
        # This parameter is required.
        self.strategy_name = strategy_name

    def validate(self):
        if self.default_addr_pool:
            for v1 in self.default_addr_pool:
                 if v1:
                    v1.validate()
        if self.failover_addr_pool:
            for v1 in self.failover_addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DefaultAddrPool'] = []
        if self.default_addr_pool is not None:
            for k1 in self.default_addr_pool:
                result['DefaultAddrPool'].append(k1.to_map() if k1 else None)

        if self.default_addr_pool_type is not None:
            result['DefaultAddrPoolType'] = self.default_addr_pool_type

        if self.default_latency_optimization is not None:
            result['DefaultLatencyOptimization'] = self.default_latency_optimization

        if self.default_lba_strategy is not None:
            result['DefaultLbaStrategy'] = self.default_lba_strategy

        if self.default_max_return_addr_num is not None:
            result['DefaultMaxReturnAddrNum'] = self.default_max_return_addr_num

        if self.default_min_available_addr_num is not None:
            result['DefaultMinAvailableAddrNum'] = self.default_min_available_addr_num

        result['FailoverAddrPool'] = []
        if self.failover_addr_pool is not None:
            for k1 in self.failover_addr_pool:
                result['FailoverAddrPool'].append(k1.to_map() if k1 else None)

        if self.failover_addr_pool_type is not None:
            result['FailoverAddrPoolType'] = self.failover_addr_pool_type

        if self.failover_latency_optimization is not None:
            result['FailoverLatencyOptimization'] = self.failover_latency_optimization

        if self.failover_lba_strategy is not None:
            result['FailoverLbaStrategy'] = self.failover_lba_strategy

        if self.failover_max_return_addr_num is not None:
            result['FailoverMaxReturnAddrNum'] = self.failover_max_return_addr_num

        if self.failover_min_available_addr_num is not None:
            result['FailoverMinAvailableAddrNum'] = self.failover_min_available_addr_num

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.lines is not None:
            result['Lines'] = self.lines

        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.default_addr_pool = []
        if m.get('DefaultAddrPool') is not None:
            for k1 in m.get('DefaultAddrPool'):
                temp_model = main_models.AddDnsGtmAccessStrategyRequestDefaultAddrPool()
                self.default_addr_pool.append(temp_model.from_map(k1))

        if m.get('DefaultAddrPoolType') is not None:
            self.default_addr_pool_type = m.get('DefaultAddrPoolType')

        if m.get('DefaultLatencyOptimization') is not None:
            self.default_latency_optimization = m.get('DefaultLatencyOptimization')

        if m.get('DefaultLbaStrategy') is not None:
            self.default_lba_strategy = m.get('DefaultLbaStrategy')

        if m.get('DefaultMaxReturnAddrNum') is not None:
            self.default_max_return_addr_num = m.get('DefaultMaxReturnAddrNum')

        if m.get('DefaultMinAvailableAddrNum') is not None:
            self.default_min_available_addr_num = m.get('DefaultMinAvailableAddrNum')

        self.failover_addr_pool = []
        if m.get('FailoverAddrPool') is not None:
            for k1 in m.get('FailoverAddrPool'):
                temp_model = main_models.AddDnsGtmAccessStrategyRequestFailoverAddrPool()
                self.failover_addr_pool.append(temp_model.from_map(k1))

        if m.get('FailoverAddrPoolType') is not None:
            self.failover_addr_pool_type = m.get('FailoverAddrPoolType')

        if m.get('FailoverLatencyOptimization') is not None:
            self.failover_latency_optimization = m.get('FailoverLatencyOptimization')

        if m.get('FailoverLbaStrategy') is not None:
            self.failover_lba_strategy = m.get('FailoverLbaStrategy')

        if m.get('FailoverMaxReturnAddrNum') is not None:
            self.failover_max_return_addr_num = m.get('FailoverMaxReturnAddrNum')

        if m.get('FailoverMinAvailableAddrNum') is not None:
            self.failover_min_available_addr_num = m.get('FailoverMinAvailableAddrNum')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Lines') is not None:
            self.lines = m.get('Lines')

        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

class AddDnsGtmAccessStrategyRequestFailoverAddrPool(DaraModel):
    def __init__(
        self,
        id: str = None,
        lba_weight: int = None,
    ):
        # The ID of the address pool.
        self.id = id
        # The weight of the address pool.
        self.lba_weight = lba_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        return self

class AddDnsGtmAccessStrategyRequestDefaultAddrPool(DaraModel):
    def __init__(
        self,
        id: str = None,
        lba_weight: int = None,
    ):
        # The ID of the address pool.
        self.id = id
        # The weight of the address pool.
        self.lba_weight = lba_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        return self

