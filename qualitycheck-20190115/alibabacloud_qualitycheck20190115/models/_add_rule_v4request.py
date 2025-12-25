# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRuleV4Request(DaraModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        is_copy: bool = None,
        json_str_for_rule: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.is_copy = is_copy
        # This parameter is required.
        self.json_str_for_rule = json_str_for_rule

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')

        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')

        if m.get('JsonStrForRule') is not None:
            self.json_str_for_rule = m.get('JsonStrForRule')

        return self

