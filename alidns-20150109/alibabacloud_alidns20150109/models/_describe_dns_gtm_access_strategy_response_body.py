# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsGtmAccessStrategyResponseBody(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        default_addr_pool_group_status: str = None,
        default_addr_pool_type: str = None,
        default_addr_pools: main_models.DescribeDnsGtmAccessStrategyResponseBodyDefaultAddrPools = None,
        default_available_addr_num: int = None,
        default_latency_optimization: str = None,
        default_lba_strategy: str = None,
        default_max_return_addr_num: int = None,
        default_min_available_addr_num: int = None,
        effective_addr_pool_group_type: str = None,
        failover_addr_pool_group_status: str = None,
        failover_addr_pool_type: str = None,
        failover_addr_pools: main_models.DescribeDnsGtmAccessStrategyResponseBodyFailoverAddrPools = None,
        failover_available_addr_num: int = None,
        failover_latency_optimization: str = None,
        failover_lba_strategy: str = None,
        failover_max_return_addr_num: int = None,
        failover_min_available_addr_num: int = None,
        instance_id: str = None,
        lines: main_models.DescribeDnsGtmAccessStrategyResponseBodyLines = None,
        request_id: str = None,
        strategy_id: str = None,
        strategy_mode: str = None,
        strategy_name: str = None,
    ):
        # The primary/secondary switchover policy for address pool groups. Valid values:
        # 
        # *   AUTO: performs automatic switchover between the primary and secondary address pool groups upon failures.
        # *   DEFAULT: uses the primary address pool group.
        # *   FAILOVER: uses the secondary address pool group.
        self.access_mode = access_mode
        # The time when the access policy was created.
        self.create_time = create_time
        # The timestamp that indicates when the access policy was created.
        self.create_timestamp = create_timestamp
        # The status of the primary address pool group. Valid values:
        # 
        # *   AVAILABLE: available
        # *   NOT_AVAILABLE: unavailable
        self.default_addr_pool_group_status = default_addr_pool_group_status
        # The type of the primary address pool. Valid values:
        # 
        # *   IPV4
        # *   IPV6
        # *   DOMAIN
        self.default_addr_pool_type = default_addr_pool_type
        # The address pools in the primary address pool group.
        self.default_addr_pools = default_addr_pools
        # The number of available addresses in the primary address pool.
        self.default_available_addr_num = default_available_addr_num
        # Indicates whether scheduling optimization for latency resolution was enabled for the primary address pool group. Valid values:
        # 
        # *   OPEN: enabled
        # *   CLOSE: disabled
        self.default_latency_optimization = default_latency_optimization
        # The load balancing policy of the primary address pool group. Valid values:
        # 
        # *   ALL_RR: returns all addresses.
        # *   RATIO: returns addresses by weight.
        self.default_lba_strategy = default_lba_strategy
        # The maximum number of addresses returned from the primary address pool group.
        self.default_max_return_addr_num = default_max_return_addr_num
        # The minimum number of available addresses in the primary address pool group.
        self.default_min_available_addr_num = default_min_available_addr_num
        # The type of the active address pool group. Valid values:
        # 
        # *   DEFAULT: the primary address pool group
        # *   FAILOVER: the secondary address pool group
        self.effective_addr_pool_group_type = effective_addr_pool_group_type
        # The status of the secondary address pool group. Valid values:
        # 
        # *   AVAILABLE: available
        # *   NOT_AVAILABLE: unavailable
        self.failover_addr_pool_group_status = failover_addr_pool_group_status
        # The type of the secondary address pool. Valid values:
        # 
        # *   IPV4
        # *   IPV6
        # *   DOMAIN
        self.failover_addr_pool_type = failover_addr_pool_type
        # The address pools in the secondary address pool group.
        self.failover_addr_pools = failover_addr_pools
        # The number of available addresses in the secondary address pool.
        self.failover_available_addr_num = failover_available_addr_num
        # Indicates whether scheduling optimization for latency resolution was enabled for the secondary address pool group. Valid values:
        # 
        # *   OPEN: enabled
        # *   CLOSE: disabled
        self.failover_latency_optimization = failover_latency_optimization
        # The load balancing policy of the secondary address pool group. Valid values:
        # 
        # *   ALL_RR: returns all addresses.
        # *   RATIO: returns addresses by weight.
        self.failover_lba_strategy = failover_lba_strategy
        # The maximum number of addresses returned from the secondary address pool group.
        self.failover_max_return_addr_num = failover_max_return_addr_num
        # The minimum number of available addresses in the secondary address pool group.
        self.failover_min_available_addr_num = failover_min_available_addr_num
        # The ID of the associated instance.
        self.instance_id = instance_id
        # The source regions.
        self.lines = lines
        # The ID of the request.
        self.request_id = request_id
        # The ID of the access policy.
        self.strategy_id = strategy_id
        # The type of the access policy. Valid values:
        # 
        # *   GEO: geographical location-based
        # *   LATENCY: latency-based
        self.strategy_mode = strategy_mode
        # The name of the access policy.
        self.strategy_name = strategy_name

    def validate(self):
        if self.default_addr_pools:
            self.default_addr_pools.validate()
        if self.failover_addr_pools:
            self.failover_addr_pools.validate()
        if self.lines:
            self.lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.default_addr_pool_group_status is not None:
            result['DefaultAddrPoolGroupStatus'] = self.default_addr_pool_group_status

        if self.default_addr_pool_type is not None:
            result['DefaultAddrPoolType'] = self.default_addr_pool_type

        if self.default_addr_pools is not None:
            result['DefaultAddrPools'] = self.default_addr_pools.to_map()

        if self.default_available_addr_num is not None:
            result['DefaultAvailableAddrNum'] = self.default_available_addr_num

        if self.default_latency_optimization is not None:
            result['DefaultLatencyOptimization'] = self.default_latency_optimization

        if self.default_lba_strategy is not None:
            result['DefaultLbaStrategy'] = self.default_lba_strategy

        if self.default_max_return_addr_num is not None:
            result['DefaultMaxReturnAddrNum'] = self.default_max_return_addr_num

        if self.default_min_available_addr_num is not None:
            result['DefaultMinAvailableAddrNum'] = self.default_min_available_addr_num

        if self.effective_addr_pool_group_type is not None:
            result['EffectiveAddrPoolGroupType'] = self.effective_addr_pool_group_type

        if self.failover_addr_pool_group_status is not None:
            result['FailoverAddrPoolGroupStatus'] = self.failover_addr_pool_group_status

        if self.failover_addr_pool_type is not None:
            result['FailoverAddrPoolType'] = self.failover_addr_pool_type

        if self.failover_addr_pools is not None:
            result['FailoverAddrPools'] = self.failover_addr_pools.to_map()

        if self.failover_available_addr_num is not None:
            result['FailoverAvailableAddrNum'] = self.failover_available_addr_num

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

        if self.lines is not None:
            result['Lines'] = self.lines.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DefaultAddrPoolGroupStatus') is not None:
            self.default_addr_pool_group_status = m.get('DefaultAddrPoolGroupStatus')

        if m.get('DefaultAddrPoolType') is not None:
            self.default_addr_pool_type = m.get('DefaultAddrPoolType')

        if m.get('DefaultAddrPools') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyResponseBodyDefaultAddrPools()
            self.default_addr_pools = temp_model.from_map(m.get('DefaultAddrPools'))

        if m.get('DefaultAvailableAddrNum') is not None:
            self.default_available_addr_num = m.get('DefaultAvailableAddrNum')

        if m.get('DefaultLatencyOptimization') is not None:
            self.default_latency_optimization = m.get('DefaultLatencyOptimization')

        if m.get('DefaultLbaStrategy') is not None:
            self.default_lba_strategy = m.get('DefaultLbaStrategy')

        if m.get('DefaultMaxReturnAddrNum') is not None:
            self.default_max_return_addr_num = m.get('DefaultMaxReturnAddrNum')

        if m.get('DefaultMinAvailableAddrNum') is not None:
            self.default_min_available_addr_num = m.get('DefaultMinAvailableAddrNum')

        if m.get('EffectiveAddrPoolGroupType') is not None:
            self.effective_addr_pool_group_type = m.get('EffectiveAddrPoolGroupType')

        if m.get('FailoverAddrPoolGroupStatus') is not None:
            self.failover_addr_pool_group_status = m.get('FailoverAddrPoolGroupStatus')

        if m.get('FailoverAddrPoolType') is not None:
            self.failover_addr_pool_type = m.get('FailoverAddrPoolType')

        if m.get('FailoverAddrPools') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyResponseBodyFailoverAddrPools()
            self.failover_addr_pools = temp_model.from_map(m.get('FailoverAddrPools'))

        if m.get('FailoverAvailableAddrNum') is not None:
            self.failover_available_addr_num = m.get('FailoverAvailableAddrNum')

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

        if m.get('Lines') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyResponseBodyLines()
            self.lines = temp_model.from_map(m.get('Lines'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

class DescribeDnsGtmAccessStrategyResponseBodyLines(DaraModel):
    def __init__(
        self,
        line: List[main_models.DescribeDnsGtmAccessStrategyResponseBodyLinesLine] = None,
    ):
        self.line = line

    def validate(self):
        if self.line:
            for v1 in self.line:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Line'] = []
        if self.line is not None:
            for k1 in self.line:
                result['Line'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line = []
        if m.get('Line') is not None:
            for k1 in m.get('Line'):
                temp_model = main_models.DescribeDnsGtmAccessStrategyResponseBodyLinesLine()
                self.line.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategyResponseBodyLinesLine(DaraModel):
    def __init__(
        self,
        group_code: str = None,
        group_name: str = None,
        line_code: str = None,
        line_name: str = None,
    ):
        # The code of the source region group.
        self.group_code = group_code
        # The name of the source region group.
        self.group_name = group_name
        # The line code of the source region.
        self.line_code = line_code
        # The line name of the source region.
        self.line_name = line_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.line_name is not None:
            result['LineName'] = self.line_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')

        return self

class DescribeDnsGtmAccessStrategyResponseBodyFailoverAddrPools(DaraModel):
    def __init__(
        self,
        failover_addr_pool: List[main_models.DescribeDnsGtmAccessStrategyResponseBodyFailoverAddrPoolsFailoverAddrPool] = None,
    ):
        self.failover_addr_pool = failover_addr_pool

    def validate(self):
        if self.failover_addr_pool:
            for v1 in self.failover_addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailoverAddrPool'] = []
        if self.failover_addr_pool is not None:
            for k1 in self.failover_addr_pool:
                result['FailoverAddrPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failover_addr_pool = []
        if m.get('FailoverAddrPool') is not None:
            for k1 in m.get('FailoverAddrPool'):
                temp_model = main_models.DescribeDnsGtmAccessStrategyResponseBodyFailoverAddrPoolsFailoverAddrPool()
                self.failover_addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategyResponseBodyFailoverAddrPoolsFailoverAddrPool(DaraModel):
    def __init__(
        self,
        addr_count: int = None,
        id: str = None,
        lba_weight: int = None,
        name: str = None,
    ):
        # The number of addresses in the address pool.
        self.addr_count = addr_count
        # The ID of the address pool.
        self.id = id
        # The weight of the address pool.
        self.lba_weight = lba_weight
        # The name of the address pool.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count

        if self.id is not None:
            result['Id'] = self.id

        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeDnsGtmAccessStrategyResponseBodyDefaultAddrPools(DaraModel):
    def __init__(
        self,
        default_addr_pool: List[main_models.DescribeDnsGtmAccessStrategyResponseBodyDefaultAddrPoolsDefaultAddrPool] = None,
    ):
        self.default_addr_pool = default_addr_pool

    def validate(self):
        if self.default_addr_pool:
            for v1 in self.default_addr_pool:
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.default_addr_pool = []
        if m.get('DefaultAddrPool') is not None:
            for k1 in m.get('DefaultAddrPool'):
                temp_model = main_models.DescribeDnsGtmAccessStrategyResponseBodyDefaultAddrPoolsDefaultAddrPool()
                self.default_addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategyResponseBodyDefaultAddrPoolsDefaultAddrPool(DaraModel):
    def __init__(
        self,
        addr_count: int = None,
        id: str = None,
        lba_weight: int = None,
        name: str = None,
    ):
        # The number of addresses in the address pool.
        self.addr_count = addr_count
        # The ID of the address pool.
        self.id = id
        # The weight of the address pool.
        self.lba_weight = lba_weight
        # The name of the address pool.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count

        if self.id is not None:
            result['Id'] = self.id

        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

