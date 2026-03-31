# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevertEvaluationResultsShrinkRequest(DaraModel):
    def __init__(
        self,
        config_rule_id: str = None,
        resources_shrink: str = None,
    ):
        # The rule ID.
        # 
        # For more information about how to obtain the ID of a rule, see [ListConfigRules](https://help.aliyun.com/document_detail/169607.html).
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The resources that are to be re-evaluated.
        # 
        # This parameter is required.
        self.resources_shrink = resources_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.resources_shrink is not None:
            result['Resources'] = self.resources_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('Resources') is not None:
            self.resources_shrink = m.get('Resources')

        return self

