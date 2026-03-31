# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAggregateConfigRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        tag_shrink: str = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The ID of the rule.
        # 
        # You can call the [ListAggregateConfigRules](https://help.aliyun.com/document_detail/264148.html) operation to obtain the rule ID.
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag_shrink = tag_shrink

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

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

