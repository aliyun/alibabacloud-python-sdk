# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmAccessStrategiesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        strategies: main_models.DescribeGtmAccessStrategiesResponseBodyStrategies = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The number of the page returned.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The returned list of access policies of the GTM instance.
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
            temp_model = main_models.DescribeGtmAccessStrategiesResponseBodyStrategies()
            self.strategies = temp_model.from_map(m.get('Strategies'))

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeGtmAccessStrategiesResponseBodyStrategies(DaraModel):
    def __init__(
        self,
        strategy: List[main_models.DescribeGtmAccessStrategiesResponseBodyStrategiesStrategy] = None,
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
                temp_model = main_models.DescribeGtmAccessStrategiesResponseBodyStrategiesStrategy()
                self.strategy.append(temp_model.from_map(k1))

        return self

class DescribeGtmAccessStrategiesResponseBodyStrategiesStrategy(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        access_status: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        default_addr_pool_id: str = None,
        default_addr_pool_monitor_status: str = None,
        default_addr_pool_name: str = None,
        default_addr_pool_status: str = None,
        failover_addr_pool_id: str = None,
        failover_addr_pool_monitor_status: str = None,
        failover_addr_pool_name: str = None,
        failover_addr_pool_status: str = None,
        instance_id: str = None,
        lines: main_models.DescribeGtmAccessStrategiesResponseBodyStrategiesStrategyLines = None,
        strategy_id: str = None,
        strategy_mode: str = None,
        strategy_name: str = None,
    ):
        # The access policy. Valid values:
        # 
        # *   **AUTO**: Automatic switch
        # *   **DEFAULT**: Default address pool
        # *   **FAILOVER**: Failover address pool
        self.access_mode = access_mode
        # The access status. Valid values:
        # 
        # *   **DEFAULT**: The default address pool is currently accessed.
        # *   **FAILOVER**: The failover address pool is currently accessed.
        self.access_status = access_status
        # The time when the access policy was created.
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        # The ID of the default address pool.
        self.default_addr_pool_id = default_addr_pool_id
        # Indicates whether health check was enabled for the default address pool. Valid values:
        # 
        # *   **OPEN**: Enabled
        # *   **CLOSE**: Disabled
        # *   **UNCONFIGURED**: Not configured
        self.default_addr_pool_monitor_status = default_addr_pool_monitor_status
        # The name of the default address pool.
        self.default_addr_pool_name = default_addr_pool_name
        # The availability status of the default address pool. Valid values:
        # 
        # *   **AVAILABLE**: Available
        # *   **NOT_AVAILABLE**: Unavailable
        self.default_addr_pool_status = default_addr_pool_status
        # The ID of the failover address pool.
        self.failover_addr_pool_id = failover_addr_pool_id
        # Indicates whether health check was enabled for the failover address pool.
        self.failover_addr_pool_monitor_status = failover_addr_pool_monitor_status
        # The name of the failover address pool.
        self.failover_addr_pool_name = failover_addr_pool_name
        # The availability status of the failover address pool.
        self.failover_addr_pool_status = failover_addr_pool_status
        # The ID of the GTM instance whose access policies you want to query.
        self.instance_id = instance_id
        # The returned lines of access regions.
        self.lines = lines
        # The ID of the access policy.
        self.strategy_id = strategy_id
        # The mode of the access policy. **SELF_DEFINED** indicates that the access policy is user-defined.
        self.strategy_mode = strategy_mode
        # The name of the access policy.
        self.strategy_name = strategy_name

    def validate(self):
        if self.lines:
            self.lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        if self.access_status is not None:
            result['AccessStatus'] = self.access_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.default_addr_pool_id is not None:
            result['DefaultAddrPoolId'] = self.default_addr_pool_id

        if self.default_addr_pool_monitor_status is not None:
            result['DefaultAddrPoolMonitorStatus'] = self.default_addr_pool_monitor_status

        if self.default_addr_pool_name is not None:
            result['DefaultAddrPoolName'] = self.default_addr_pool_name

        if self.default_addr_pool_status is not None:
            result['DefaultAddrPoolStatus'] = self.default_addr_pool_status

        if self.failover_addr_pool_id is not None:
            result['FailoverAddrPoolId'] = self.failover_addr_pool_id

        if self.failover_addr_pool_monitor_status is not None:
            result['FailoverAddrPoolMonitorStatus'] = self.failover_addr_pool_monitor_status

        if self.failover_addr_pool_name is not None:
            result['FailoverAddrPoolName'] = self.failover_addr_pool_name

        if self.failover_addr_pool_status is not None:
            result['FailoverAddrPoolStatus'] = self.failover_addr_pool_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lines is not None:
            result['Lines'] = self.lines.to_map()

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

        if m.get('AccessStatus') is not None:
            self.access_status = m.get('AccessStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DefaultAddrPoolId') is not None:
            self.default_addr_pool_id = m.get('DefaultAddrPoolId')

        if m.get('DefaultAddrPoolMonitorStatus') is not None:
            self.default_addr_pool_monitor_status = m.get('DefaultAddrPoolMonitorStatus')

        if m.get('DefaultAddrPoolName') is not None:
            self.default_addr_pool_name = m.get('DefaultAddrPoolName')

        if m.get('DefaultAddrPoolStatus') is not None:
            self.default_addr_pool_status = m.get('DefaultAddrPoolStatus')

        if m.get('FailoverAddrPoolId') is not None:
            self.failover_addr_pool_id = m.get('FailoverAddrPoolId')

        if m.get('FailoverAddrPoolMonitorStatus') is not None:
            self.failover_addr_pool_monitor_status = m.get('FailoverAddrPoolMonitorStatus')

        if m.get('FailoverAddrPoolName') is not None:
            self.failover_addr_pool_name = m.get('FailoverAddrPoolName')

        if m.get('FailoverAddrPoolStatus') is not None:
            self.failover_addr_pool_status = m.get('FailoverAddrPoolStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lines') is not None:
            temp_model = main_models.DescribeGtmAccessStrategiesResponseBodyStrategiesStrategyLines()
            self.lines = temp_model.from_map(m.get('Lines'))

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

class DescribeGtmAccessStrategiesResponseBodyStrategiesStrategyLines(DaraModel):
    def __init__(
        self,
        line: List[main_models.DescribeGtmAccessStrategiesResponseBodyStrategiesStrategyLinesLine] = None,
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
                temp_model = main_models.DescribeGtmAccessStrategiesResponseBodyStrategiesStrategyLinesLine()
                self.line.append(temp_model.from_map(k1))

        return self

class DescribeGtmAccessStrategiesResponseBodyStrategiesStrategyLinesLine(DaraModel):
    def __init__(
        self,
        group_code: str = None,
        group_name: str = None,
        line_code: str = None,
        line_name: str = None,
    ):
        # The code of the access region group.
        self.group_code = group_code
        # The name of the access region group.
        self.group_name = group_name
        # The code for the line of the access region.
        self.line_code = line_code
        # The name for the line of the access region.
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

