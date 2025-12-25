# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRuleRequest(DaraModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        force_delete: bool = None,
        is_scheme_data: int = None,
        rule_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.force_delete = force_delete
        self.is_scheme_data = is_scheme_data
        # This parameter is required.
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

        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete

        if self.is_scheme_data is not None:
            result['IsSchemeData'] = self.is_scheme_data

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')

        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')

        if m.get('IsSchemeData') is not None:
            self.is_scheme_data = m.get('IsSchemeData')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

