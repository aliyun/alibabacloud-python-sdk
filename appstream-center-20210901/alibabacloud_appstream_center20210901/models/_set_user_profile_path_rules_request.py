# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetUserProfilePathRulesRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_set_id: str = None,
        region_id: str = None,
        user_profile_path_rules: str = None,
        user_profile_rule_type: str = None,
    ):
        # The ID of a single app instance group. This parameter and AppInstanceGroupSetId are mutually exclusive. If a cloud app or cloud browser app instance group belongs to an enabled set, you must configure the rules at the set level.
        self.app_instance_group_id = app_instance_group_id
        # The ID of an enabled app instance group set. This parameter and AppInstanceGroupId are mutually exclusive. You can set rules for up to 200 member app instance groups at a time.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The region ID of the request. When you query or set rules for a specified app instance group, use the region where the target app instance group resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The JSON array string of the complete rule list. Each item uses `blackPath` to specify the excluded path and `whitePaths` to specify the relative paths that still require roaming within the excluded directory. The path type `file` indicates a file, and `folder` indicates a directory.
        self.user_profile_path_rules = user_profile_path_rules
        # The type of rule to set. Set this parameter to `AppInstanceGroup` when you configure rules for an app instance group or an app instance group set.
        # 
        # This parameter is required.
        self.user_profile_rule_type = user_profile_rule_type

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

        if self.user_profile_path_rules is not None:
            result['UserProfilePathRules'] = self.user_profile_path_rules

        if self.user_profile_rule_type is not None:
            result['UserProfileRuleType'] = self.user_profile_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupSetId') is not None:
            self.app_instance_group_set_id = m.get('AppInstanceGroupSetId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserProfilePathRules') is not None:
            self.user_profile_path_rules = m.get('UserProfilePathRules')

        if m.get('UserProfileRuleType') is not None:
            self.user_profile_rule_type = m.get('UserProfileRuleType')

        return self

