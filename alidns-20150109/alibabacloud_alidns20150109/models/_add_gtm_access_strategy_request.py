# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddGtmAccessStrategyRequest(DaraModel):
    def __init__(
        self,
        access_lines: str = None,
        default_addr_pool_id: str = None,
        failover_addr_pool_id: str = None,
        instance_id: str = None,
        lang: str = None,
        strategy_name: str = None,
    ):
        # The line codes of access regions.
        # 
        # This parameter is required.
        self.access_lines = access_lines
        # The ID of the default address pool.
        # 
        # This parameter is required.
        self.default_addr_pool_id = default_addr_pool_id
        # The ID of the failover address pool.
        # 
        # If the failover address pool is not set, pass the **Empty** value.
        # 
        # This parameter is required.
        self.failover_addr_pool_id = failover_addr_pool_id
        # The ID of the GTM instance for which you want to create an access policy.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language used by the user.
        self.lang = lang
        # The name of the access policy.
        # 
        # This parameter is required.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

