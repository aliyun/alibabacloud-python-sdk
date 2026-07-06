# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyScheduledScalingRuleRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        instance_id: str = None,
        region_id: str = None,
        rule_name: str = None,
    ):
        # Enable or disable the scheduled task policy. Valid values:
        # 
        # - **true**: Enable.
        # 
        # - **false**: Disable.
        # 
        # > For a one-time scheduling policy type, the start execution time must be more than 30 minutes later than the current time for the policy to be enabled.
        # 
        # This parameter is required.
        self.enable = enable
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The policy name.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

