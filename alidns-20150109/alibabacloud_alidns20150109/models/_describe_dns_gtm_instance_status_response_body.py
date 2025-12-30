# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsGtmInstanceStatusResponseBody(DaraModel):
    def __init__(
        self,
        addr_available_num: int = None,
        addr_not_available_num: int = None,
        addr_pool_group_not_available_num: int = None,
        request_id: str = None,
        strategy_not_available_num: int = None,
        switch_to_failover_strategy_num: int = None,
    ):
        # The number of available addresses.
        self.addr_available_num = addr_available_num
        # The number of unavailable addresses.
        self.addr_not_available_num = addr_not_available_num
        # The number of unavailable address pool groups.
        self.addr_pool_group_not_available_num = addr_pool_group_not_available_num
        # The ID of the request.
        self.request_id = request_id
        # The number of access policies that are unavailable in the current active address pool group.
        self.strategy_not_available_num = strategy_not_available_num
        # The number of access policies switched to the secondary address pool group.
        self.switch_to_failover_strategy_num = switch_to_failover_strategy_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_available_num is not None:
            result['AddrAvailableNum'] = self.addr_available_num

        if self.addr_not_available_num is not None:
            result['AddrNotAvailableNum'] = self.addr_not_available_num

        if self.addr_pool_group_not_available_num is not None:
            result['AddrPoolGroupNotAvailableNum'] = self.addr_pool_group_not_available_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.strategy_not_available_num is not None:
            result['StrategyNotAvailableNum'] = self.strategy_not_available_num

        if self.switch_to_failover_strategy_num is not None:
            result['SwitchToFailoverStrategyNum'] = self.switch_to_failover_strategy_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrAvailableNum') is not None:
            self.addr_available_num = m.get('AddrAvailableNum')

        if m.get('AddrNotAvailableNum') is not None:
            self.addr_not_available_num = m.get('AddrNotAvailableNum')

        if m.get('AddrPoolGroupNotAvailableNum') is not None:
            self.addr_pool_group_not_available_num = m.get('AddrPoolGroupNotAvailableNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StrategyNotAvailableNum') is not None:
            self.strategy_not_available_num = m.get('StrategyNotAvailableNum')

        if m.get('SwitchToFailoverStrategyNum') is not None:
            self.switch_to_failover_strategy_num = m.get('SwitchToFailoverStrategyNum')

        return self

