# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsGtmAccessStrategiesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        strategies: main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategies = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The access policies.
        self.strategies = strategies
        # The total number of entries returned on all pages.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.strategies:
            self.strategies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.strategies is not None:
            result['Strategies'] = self.strategies.to_map()

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Strategies') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategies()
            self.strategies = temp_model.from_map(m.get('Strategies'))

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeDnsGtmAccessStrategiesResponseBodyStrategies(DaraModel):
    def __init__(
        self,
        strategy: List[main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategy] = None,
    ):
        self.strategy = strategy

    def validate(self):
        if self.strategy:
            for v1 in self.strategy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Strategy'] = []
        if self.strategy is not None:
            for k1 in self.strategy:
                result['Strategy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.strategy = []
        if m.get('Strategy') is not None:
            for k1 in m.get('Strategy'):
                temp_model = main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategy()
                self.strategy.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategy(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        effective_addr_pool_group_type: str = None,
        effective_addr_pool_type: str = None,
        effective_addr_pools: main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyEffectiveAddrPools = None,
        effective_lba_strategy: str = None,
        lines: main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyLines = None,
        strategy_id: str = None,
        strategy_name: str = None,
    ):
        # The time when the access policy was created.
        self.create_time = create_time
        # The timestamp that indicates when the access policy was created.
        self.create_timestamp = create_timestamp
        # The type of the active address pool group. Valid values:
        # 
        # *   DEFAULT: the primary address pool group
        # *   FAILOVER: the secondary address pool group
        self.effective_addr_pool_group_type = effective_addr_pool_group_type
        # The type of the active address pools. Valid values:
        # 
        # *   IPV4
        # *   IPV6
        # *   DOMAIN
        self.effective_addr_pool_type = effective_addr_pool_type
        # The active address pool groups.
        self.effective_addr_pools = effective_addr_pools
        # The load balancing policy of the active address pool group. Data is returned when StrategyMode is set to GEO. Valid values: 
        # 
        # - ALL_RR: returns all addresses.
        # - RATIO: returns addresses by weight.
        self.effective_lba_strategy = effective_lba_strategy
        # The source regions. Data is returned when StrategyMode is set to GEO. Valid values:
        self.lines = lines
        # The ID of the access policy.
        self.strategy_id = strategy_id
        # The name of the access policy.
        self.strategy_name = strategy_name

    def validate(self):
        if self.effective_addr_pools:
            self.effective_addr_pools.validate()
        if self.lines:
            self.lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.effective_addr_pool_group_type is not None:
            result['EffectiveAddrPoolGroupType'] = self.effective_addr_pool_group_type

        if self.effective_addr_pool_type is not None:
            result['EffectiveAddrPoolType'] = self.effective_addr_pool_type

        if self.effective_addr_pools is not None:
            result['EffectiveAddrPools'] = self.effective_addr_pools.to_map()

        if self.effective_lba_strategy is not None:
            result['EffectiveLbaStrategy'] = self.effective_lba_strategy

        if self.lines is not None:
            result['Lines'] = self.lines.to_map()

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('EffectiveAddrPoolGroupType') is not None:
            self.effective_addr_pool_group_type = m.get('EffectiveAddrPoolGroupType')

        if m.get('EffectiveAddrPoolType') is not None:
            self.effective_addr_pool_type = m.get('EffectiveAddrPoolType')

        if m.get('EffectiveAddrPools') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyEffectiveAddrPools()
            self.effective_addr_pools = temp_model.from_map(m.get('EffectiveAddrPools'))

        if m.get('EffectiveLbaStrategy') is not None:
            self.effective_lba_strategy = m.get('EffectiveLbaStrategy')

        if m.get('Lines') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyLines()
            self.lines = temp_model.from_map(m.get('Lines'))

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

class DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyLines(DaraModel):
    def __init__(
        self,
        line: List[main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyLinesLine] = None,
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
                temp_model = main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyLinesLine()
                self.line.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyLinesLine(DaraModel):
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

class DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyEffectiveAddrPools(DaraModel):
    def __init__(
        self,
        effective_addr_pool: List[main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyEffectiveAddrPoolsEffectiveAddrPool] = None,
    ):
        self.effective_addr_pool = effective_addr_pool

    def validate(self):
        if self.effective_addr_pool:
            for v1 in self.effective_addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EffectiveAddrPool'] = []
        if self.effective_addr_pool is not None:
            for k1 in self.effective_addr_pool:
                result['EffectiveAddrPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.effective_addr_pool = []
        if m.get('EffectiveAddrPool') is not None:
            for k1 in m.get('EffectiveAddrPool'):
                temp_model = main_models.DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyEffectiveAddrPoolsEffectiveAddrPool()
                self.effective_addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategiesResponseBodyStrategiesStrategyEffectiveAddrPoolsEffectiveAddrPool(DaraModel):
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

