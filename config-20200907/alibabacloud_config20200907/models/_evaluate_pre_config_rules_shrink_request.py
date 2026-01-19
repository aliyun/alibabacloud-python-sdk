# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluatePreConfigRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        enable_managed_rules: bool = None,
        resource_evaluate_items_shrink: str = None,
        resource_type_format: str = None,
    ):
        # Specifies whether to enable the managed rule. Valid values:
        # 
        # *   true: enables the managed rule.
        # *   false: does not enable the managed rule. This is the default value.
        # 
        # >  After you create an evaluation rule, a managed rule that has the same settings as the evaluation rule is created. After you create a resource, the managed rule can be used to continuously check the compliance of the resource.
        self.enable_managed_rules = enable_managed_rules
        # The resources that you want to evaluate.
        # 
        # This parameter is required.
        self.resource_evaluate_items_shrink = resource_evaluate_items_shrink
        # 下一个查询开始Token
        self.resource_type_format = resource_type_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_managed_rules is not None:
            result['EnableManagedRules'] = self.enable_managed_rules

        if self.resource_evaluate_items_shrink is not None:
            result['ResourceEvaluateItems'] = self.resource_evaluate_items_shrink

        if self.resource_type_format is not None:
            result['ResourceTypeFormat'] = self.resource_type_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableManagedRules') is not None:
            self.enable_managed_rules = m.get('EnableManagedRules')

        if m.get('ResourceEvaluateItems') is not None:
            self.resource_evaluate_items_shrink = m.get('ResourceEvaluateItems')

        if m.get('ResourceTypeFormat') is not None:
            self.resource_type_format = m.get('ResourceTypeFormat')

        return self

