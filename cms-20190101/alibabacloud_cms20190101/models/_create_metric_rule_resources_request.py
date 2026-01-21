# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMetricRuleResourcesRequest(DaraModel):
    def __init__(
        self,
        overwrite: str = None,
        resources: str = None,
        rule_id: str = None,
    ):
        # Specifies whether to overwrite existing resources. Valid values:
        # 
        # *   true: The resources submitted this time overwrite the previously associated resources.
        # *   false: The resources submitted this time do not overwrite the previously associated resources. The associated resources after submission include the previously associated resources and the resources submitted this time.
        self.overwrite = overwrite
        # The resources that are associated with the alert rule. Set the value to a JSON array.
        # 
        # >  You can add up to 100 resources each time. An alert rule can be associated with up to 3,000 resources.
        # 
        # This parameter is required.
        self.resources = resources
        # The ID of the alert rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

