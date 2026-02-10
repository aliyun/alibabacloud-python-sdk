# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAutoTagRulesRequest(DaraModel):
    def __init__(
        self,
        rule_id_list: str = None,
    ):
        # The ID of the asset auto-tagging rule. Separate multiple IDs with commas (,).
        # 
        # >  You can call the [ListAutoTagRules](~~ListAutoTagRules~~) operation to query the ID.
        # 
        # This parameter is required.
        self.rule_id_list = rule_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id_list is not None:
            result['RuleIdList'] = self.rule_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleIdList') is not None:
            self.rule_id_list = m.get('RuleIdList')

        return self

