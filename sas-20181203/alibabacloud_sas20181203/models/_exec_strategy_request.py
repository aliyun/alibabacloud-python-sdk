# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecStrategyRequest(DaraModel):
    def __init__(
        self,
        exec_action: str = None,
        lang: str = None,
        strategy_id: int = None,
    ):
        # Set the action for this execution, default is **exec**. Values:
        # - **exec**: Execute. - **terminate**: Terminate.
        self.exec_action = exec_action
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the baseline check policy.
        # 
        # >  You can call the [DescribeStrategy](~~DescribeStrategy~~) operation to query the IDs of baseline check policies.
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec_action is not None:
            result['ExecAction'] = self.exec_action

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecAction') is not None:
            self.exec_action = m.get('ExecAction')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

