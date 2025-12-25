# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRuleV4Request(DaraModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str_for_rule: str = None,
        rule_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str_for_rule = json_str_for_rule
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id

        if self.json_str_for_rule is not None:
            result['JsonStrForRule'] = self.json_str_for_rule

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')

        if m.get('JsonStrForRule') is not None:
            self.json_str_for_rule = m.get('JsonStrForRule')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

