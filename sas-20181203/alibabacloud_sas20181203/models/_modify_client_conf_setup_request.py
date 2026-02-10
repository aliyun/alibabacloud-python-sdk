# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyClientConfSetupRequest(DaraModel):
    def __init__(
        self,
        strategy_config: str = None,
        strategy_tag: str = None,
        strategy_tag_value: str = None,
    ):
        # The configurations of the Security Center agent.
        # 
        # *   cpu: the maximum CPU utilization that can be occupied by the Security Center agent on the server
        # *   mem: the maximum memory usage that can be occupied by the Security Center agent on the server
        self.strategy_config = strategy_config
        # The type of the tag.
        # 
        # This parameter is required.
        self.strategy_tag = strategy_tag
        # The value of the tag. Valid values:
        # 
        # *   major
        # *   advanced
        # *   basic
        # 
        # This parameter is required.
        self.strategy_tag_value = strategy_tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strategy_config is not None:
            result['StrategyConfig'] = self.strategy_config

        if self.strategy_tag is not None:
            result['StrategyTag'] = self.strategy_tag

        if self.strategy_tag_value is not None:
            result['StrategyTagValue'] = self.strategy_tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyConfig') is not None:
            self.strategy_config = m.get('StrategyConfig')

        if m.get('StrategyTag') is not None:
            self.strategy_tag = m.get('StrategyTag')

        if m.get('StrategyTagValue') is not None:
            self.strategy_tag_value = m.get('StrategyTagValue')

        return self

