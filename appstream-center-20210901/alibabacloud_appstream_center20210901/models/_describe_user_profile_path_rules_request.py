# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserProfilePathRulesRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_set_id: str = None,
        region_id: str = None,
        rule_type: str = None,
    ):
        # The ID of the app instance group. Specify either this parameter or AppInstanceGroupSetId when querying app instance group rules. This parameter can be omitted when querying system default rules.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the app instance group set. Specify either this parameter or AppInstanceGroupId when querying app instance group set rules. This parameter can be omitted when querying system default rules.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The region ID of the request. When querying or setting the rules for a specified app instance group, use the region where the target app instance group is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The path rule type. Valid values:
        # - Default: Queries the system default rules. Both target IDs can be omitted.
        # - AppInstanceGroup: Queries the rules of an app instance group or an app instance group set.
        # 
        # This parameter is required.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_set_id is not None:
            result['AppInstanceGroupSetId'] = self.app_instance_group_set_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupSetId') is not None:
            self.app_instance_group_set_id = m.get('AppInstanceGroupSetId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

