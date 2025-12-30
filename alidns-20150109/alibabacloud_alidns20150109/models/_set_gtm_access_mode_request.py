# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetGtmAccessModeRequest(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        lang: str = None,
        strategy_id: str = None,
    ):
        # The desired access policy. Valid values:
        # 
        # *   **AUTO: performs automatic switchover between the primary and secondary address pool sets upon failures.**
        # *   **DEFAULT: specifies the primary address pool set.**
        # *   **FAILOVER: specifies the secondary address pool set.
        # 
        # This parameter is required.
        self.access_mode = access_mode
        # The language.
        self.lang = lang
        # The ID of the access policy.
        # 
        # This parameter is required.
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

