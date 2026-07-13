# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckRulesRequest(DaraModel):
    def __init__(
        self,
        resource_arn: str = None,
        rule_id: str = None,
    ):
        # The unique identifier of the resource.
        # 
        # This parameter is required.
        self.resource_arn = resource_arn
        # The ID of the rule to update. If you do not specify this parameter, all rules are updated.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

