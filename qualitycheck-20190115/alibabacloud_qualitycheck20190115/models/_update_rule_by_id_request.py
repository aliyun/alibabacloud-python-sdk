# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRuleByIdRequest(DaraModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        is_copy: bool = None,
        json_str_for_rule: str = None,
        return_related_schemes: bool = None,
        rule_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.is_copy = is_copy
        # This parameter is required.
        self.json_str_for_rule = json_str_for_rule
        self.return_related_schemes = return_related_schemes
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

        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy

        if self.json_str_for_rule is not None:
            result['JsonStrForRule'] = self.json_str_for_rule

        if self.return_related_schemes is not None:
            result['ReturnRelatedSchemes'] = self.return_related_schemes

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')

        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')

        if m.get('JsonStrForRule') is not None:
            self.json_str_for_rule = m.get('JsonStrForRule')

        if m.get('ReturnRelatedSchemes') is not None:
            self.return_related_schemes = m.get('ReturnRelatedSchemes')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

