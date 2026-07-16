# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmAccessStrategyResponseBody(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        access_status: str = None,
        default_addr_pool_monitor_status: str = None,
        default_addr_pool_name: str = None,
        default_addr_pool_status: str = None,
        defult_addr_pool_id: str = None,
        failover_addr_pool_id: str = None,
        failover_addr_pool_monitor_status: str = None,
        failover_addr_pool_name: str = None,
        failover_addr_pool_status: str = None,
        instance_id: str = None,
        lines: main_models.DescribeGtmAccessStrategyResponseBodyLines = None,
        request_id: str = None,
        strategy_id: str = None,
        strategy_mode: str = None,
        strategy_name: str = None,
    ):
        # The switchover policy for the address pool groups:
        # 
        # - **AUTO**: Automatic switchover
        # 
        # - **DEFAULT**: Primary address pool group
        # 
        # - **FAILOVER**: Secondary address pool group
        self.access_mode = access_mode
        # The access status. Valid values:
        # 
        # - **DEFAULT**: Normal. Access requests are routed to the primary address pool group.
        # 
        # - **FAILOVER**: Abnormal. Access requests are routed to the secondary address pool group.
        self.access_status = access_status
        # The health check status of the primary address pool group. Valid values:
        # 
        # - **OPEN**: Enabled
        # 
        # - **CLOSE**: Disabled
        # 
        # - **UNCONFIGURED**: Not configured
        self.default_addr_pool_monitor_status = default_addr_pool_monitor_status
        # The name of the primary address pool group.
        self.default_addr_pool_name = default_addr_pool_name
        # The availability status of the primary address pool group. Valid values:
        # 
        # - **AVAILABLE**: The address pool group is available.
        # 
        # - **NOT_AVAILABLE**: The address pool group is unavailable.
        self.default_addr_pool_status = default_addr_pool_status
        # The ID of the primary address pool group.
        self.defult_addr_pool_id = defult_addr_pool_id
        # The ID of the secondary address pool group. If no secondary address pool group is configured, **EMPTY** is returned.
        self.failover_addr_pool_id = failover_addr_pool_id
        # The health check status of the secondary address pool group. Valid values:
        # 
        # - **OPEN**: Enabled
        # 
        # - **CLOSE**: Disabled
        # 
        # - **UNCONFIGURED**: Not configured
        self.failover_addr_pool_monitor_status = failover_addr_pool_monitor_status
        # The name of the secondary address pool group.
        self.failover_addr_pool_name = failover_addr_pool_name
        # The availability status of the secondary address pool group. Valid values:
        # 
        # - **AVAILABLE**: The address pool group is available.
        # 
        # - **NOT_AVAILABLE**: The address pool group is unavailable.
        self.failover_addr_pool_status = failover_addr_pool_status
        # The ID of the associated Global Traffic Manager (GTM) instance.
        self.instance_id = instance_id
        self.lines = lines
        # The unique request ID.
        self.request_id = request_id
        # The policy ID.
        self.strategy_id = strategy_id
        # The policy mode. SELF_DEFINED indicates a custom policy.
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

        if self.default_addr_pool_monitor_status is not None:
            result['DefaultAddrPoolMonitorStatus'] = self.default_addr_pool_monitor_status

        if self.default_addr_pool_name is not None:
            result['DefaultAddrPoolName'] = self.default_addr_pool_name

        if self.default_addr_pool_status is not None:
            result['DefaultAddrPoolStatus'] = self.default_addr_pool_status

        if self.defult_addr_pool_id is not None:
            result['DefultAddrPoolId'] = self.defult_addr_pool_id

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

        if m.get('AccessStatus') is not None:
            self.access_status = m.get('AccessStatus')

        if m.get('DefaultAddrPoolMonitorStatus') is not None:
            self.default_addr_pool_monitor_status = m.get('DefaultAddrPoolMonitorStatus')

        if m.get('DefaultAddrPoolName') is not None:
            self.default_addr_pool_name = m.get('DefaultAddrPoolName')

        if m.get('DefaultAddrPoolStatus') is not None:
            self.default_addr_pool_status = m.get('DefaultAddrPoolStatus')

        if m.get('DefultAddrPoolId') is not None:
            self.defult_addr_pool_id = m.get('DefultAddrPoolId')

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
            temp_model = main_models.DescribeGtmAccessStrategyResponseBodyLines()
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

class DescribeGtmAccessStrategyResponseBodyLines(DaraModel):
    def __init__(
        self,
        line: List[main_models.DescribeGtmAccessStrategyResponseBodyLinesLine] = None,
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
                temp_model = main_models.DescribeGtmAccessStrategyResponseBodyLinesLine()
                self.line.append(temp_model.from_map(k1))

        return self

class DescribeGtmAccessStrategyResponseBodyLinesLine(DaraModel):
    def __init__(
        self,
        group_code: str = None,
        group_name: str = None,
        line_code: str = None,
        line_name: str = None,
    ):
        self.group_code = group_code
        self.group_name = group_name
        self.line_code = line_code
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

