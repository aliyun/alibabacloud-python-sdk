# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertInterveneRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        intervene_rule_config_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.intervene_rule_config_shrink = intervene_rule_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.intervene_rule_config_shrink is not None:
            result['InterveneRuleConfig'] = self.intervene_rule_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InterveneRuleConfig') is not None:
            self.intervene_rule_config_shrink = m.get('InterveneRuleConfig')

        return self

