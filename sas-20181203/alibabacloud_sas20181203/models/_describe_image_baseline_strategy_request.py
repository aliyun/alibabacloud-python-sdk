# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageBaselineStrategyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source: str = None,
        strategy_id: int = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The data source. Default value: default. Valid values:
        # 
        # *   **default**: queries the information about a baseline check policy for images.
        # *   **agentless**: queries the information about a baseline check policy for agentless detection.
        self.source = source
        # The ID of the baseline check policy.
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source is not None:
            result['Source'] = self.source

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

