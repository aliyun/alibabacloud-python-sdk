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
        # Specifies whether to overwrite. Valid values:
        # 
        # - true: overwrites. The resources submitted this time overwrite the previously associated resources. That is, full modification is performed.
        # 
        # - false: does not overwrite. The resources submitted this time do not overwrite the previously associated resources (the associated resources are the historical associated resources plus the resources submitted this time). That is, incremental modification is performed.
        self.overwrite = overwrite
        # The associated resources. The value is in the JSON array format.
        # > A maximum of 100 resource instances can be added at a time, and an alert rule can be associated with a maximum of 3,000 instances.
        # >
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

