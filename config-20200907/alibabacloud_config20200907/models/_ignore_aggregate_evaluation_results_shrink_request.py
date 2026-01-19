# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IgnoreAggregateEvaluationResultsShrinkRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        ignore_date: str = None,
        reason: str = None,
        resources_shrink: str = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The ID of the rule.
        # 
        # For more information about how to obtain the ID of a rule, see [ListAggregateConfigRules](https://help.aliyun.com/document_detail/264148.html).
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The date from which the system automatically re-evaluates the ignored incompliant resources.
        # 
        # >  If you leave this parameter empty, the system does not automatically re-evaluate the ignored incompliant resources. You must manually re-evaluate the ignored incompliant resources.
        self.ignore_date = ignore_date
        # The reason why you ignore the resource.
        self.reason = reason
        # The resources to be ignored.
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
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

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
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Resources') is not None:
            self.resources_shrink = m.get('Resources')

        return self

