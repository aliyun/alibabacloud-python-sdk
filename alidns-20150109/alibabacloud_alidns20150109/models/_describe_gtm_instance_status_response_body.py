# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGtmInstanceStatusResponseBody(DaraModel):
    def __init__(
        self,
        addr_not_available_num: int = None,
        addr_pool_not_available_num: int = None,
        request_id: str = None,
        status: str = None,
        status_reason: str = None,
        strategy_not_available_num: int = None,
        switch_to_failover_strategy_num: int = None,
    ):
        # The number of unavailable addresses.
        self.addr_not_available_num = addr_not_available_num
        # The number of unavailable address pools.
        self.addr_pool_not_available_num = addr_pool_not_available_num
        # The request ID.
        self.request_id = request_id
        # The state of the instance. Valid values:
        # 
        # *   ALLOW: The operation on the instance is allowed.
        # *   DENY: The operation on the instance is not allowed.
        self.status = status
        # The reasons why the instance is in the current state. Valid values:
        # 
        # *   INSTANCE_OPERATE_BLACK_LIST: The operation on the instance is not allowed.
        # *   BETA_INSTANCE: The instance is in public preview.
        self.status_reason = status_reason
        # The number of unavailable access policies.
        self.strategy_not_available_num = strategy_not_available_num
        # The number of access policies switched to the secondary address pool.
        self.switch_to_failover_strategy_num = switch_to_failover_strategy_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_not_available_num is not None:
            result['AddrNotAvailableNum'] = self.addr_not_available_num

        if self.addr_pool_not_available_num is not None:
            result['AddrPoolNotAvailableNum'] = self.addr_pool_not_available_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.strategy_not_available_num is not None:
            result['StrategyNotAvailableNum'] = self.strategy_not_available_num

        if self.switch_to_failover_strategy_num is not None:
            result['SwitchToFailoverStrategyNum'] = self.switch_to_failover_strategy_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrNotAvailableNum') is not None:
            self.addr_not_available_num = m.get('AddrNotAvailableNum')

        if m.get('AddrPoolNotAvailableNum') is not None:
            self.addr_pool_not_available_num = m.get('AddrPoolNotAvailableNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('StrategyNotAvailableNum') is not None:
            self.strategy_not_available_num = m.get('StrategyNotAvailableNum')

        if m.get('SwitchToFailoverStrategyNum') is not None:
            self.switch_to_failover_strategy_num = m.get('SwitchToFailoverStrategyNum')

        return self

