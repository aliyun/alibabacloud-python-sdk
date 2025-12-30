# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGtmAccessStrategyRequest(DaraModel):
    def __init__(
        self,
        access_lines: str = None,
        default_addr_pool_id: str = None,
        failover_addr_pool_id: str = None,
        lang: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
    ):
        # The line codes of access regions.
        self.access_lines = access_lines
        # The ID of the default address pool.
        self.default_addr_pool_id = default_addr_pool_id
        # The ID of the failover address pool.
        self.failover_addr_pool_id = failover_addr_pool_id
        # The language used by the user.
        self.lang = lang
        # The ID of the access policy that you want to query for the GTM instance.
        # 
        # This parameter is required.
        self.strategy_id = strategy_id
        # The name of the access policy.
        self.strategy_name = strategy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_lines is not None:
            result['AccessLines'] = self.access_lines

        if self.default_addr_pool_id is not None:
            result['DefaultAddrPoolId'] = self.default_addr_pool_id

        if self.failover_addr_pool_id is not None:
            result['FailoverAddrPoolId'] = self.failover_addr_pool_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLines') is not None:
            self.access_lines = m.get('AccessLines')

        if m.get('DefaultAddrPoolId') is not None:
            self.default_addr_pool_id = m.get('DefaultAddrPoolId')

        if m.get('FailoverAddrPoolId') is not None:
            self.failover_addr_pool_id = m.get('FailoverAddrPoolId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

