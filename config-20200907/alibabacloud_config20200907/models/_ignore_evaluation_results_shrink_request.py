# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IgnoreEvaluationResultsShrinkRequest(DaraModel):
    def __init__(
        self,
        config_rule_id: str = None,
        ignore_date: str = None,
        reason: str = None,
        resources_shrink: str = None,
    ):
        # The rule ID.
        # 
        # For more information about how to obtain the rule ID, see [ListConfigRules](https://help.aliyun.com/document_detail/169607.html).
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The date on which the ignored evaluation results are automatically restored.
        # 
        # > If this parameter is left empty, the ignored evaluation results are not automatically restored. You must manually restore them.
        self.ignore_date = ignore_date
        # The reason for ignoring the resources.
        self.reason = reason
        # The list of resources to be ignored.
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

        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.resources_shrink is not None:
            result['Resources'] = self.resources_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Resources') is not None:
            self.resources_shrink = m.get('Resources')

        return self

