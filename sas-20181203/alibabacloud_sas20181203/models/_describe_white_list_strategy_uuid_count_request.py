# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWhiteListStrategyUuidCountRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        strategy_id: int = None,
        type: int = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip
        # The ID of the policy.
        # 
        # >  You can call the [DescribeWhiteListStrategyStatistics](~~DescribeWhiteListStrategyStatistics~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.strategy_id = strategy_id
        # The type of the policy. Valid values:
        # 
        # *   **1**: learning policy
        # *   **2**: application policy
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

