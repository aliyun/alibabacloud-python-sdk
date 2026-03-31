# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteConfigRulesRequest(DaraModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        # The rule IDs. Separate multiple rule IDs with commas (,).
        # 
        # For more information about how to obtain the ID of a rule, see [ListConfigRules](https://help.aliyun.com/document_detail/609222.html).
        # 
        # This parameter is required.
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')

        return self

