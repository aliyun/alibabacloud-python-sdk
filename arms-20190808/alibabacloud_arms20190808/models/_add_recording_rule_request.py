# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRecordingRuleRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        rule_yaml: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The custom recording rule. The value is in the YAML format.
        # 
        # This parameter is required.
        self.rule_yaml = rule_yaml

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_yaml is not None:
            result['RuleYaml'] = self.rule_yaml

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleYaml') is not None:
            self.rule_yaml = m.get('RuleYaml')

        return self

