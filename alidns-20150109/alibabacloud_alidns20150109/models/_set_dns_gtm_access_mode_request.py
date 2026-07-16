# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDnsGtmAccessModeRequest(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        lang: str = None,
        strategy_id: str = None,
    ):
        # The switchover policy for the address pool collection:
        # 
        # - AUTO: Automatic switchover
        # 
        # - DEFAULT: The primary address pool collection
        # 
        # - FAILOVER: The secondary address pool collection
        # 
        # This parameter is required.
        self.access_mode = access_mode
        # The language of certain response parameters. Default: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The ID of the access policy. Call [DescribeDnsGtmAccessStrategies](https://help.aliyun.com/document_detail/2357191.html) to obtain the policy ID.
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

