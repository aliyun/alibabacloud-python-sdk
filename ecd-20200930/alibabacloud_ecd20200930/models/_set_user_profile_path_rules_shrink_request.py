# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetUserProfilePathRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        region_id: str = None,
        user_profile_path_rule_shrink: str = None,
        user_profile_rule_type: str = None,
    ):
        # The desktop group ID.
        self.desktop_group_id = desktop_group_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The directories that you want to configure in the blacklist and whitelist.
        self.user_profile_path_rule_shrink = user_profile_path_rule_shrink
        # The directory type that you want to configure.
        # 
        # Valid values:
        # 
        # *   Both_Default_DesktopGroup
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DesktopGroup
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Default
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.user_profile_rule_type = user_profile_rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_profile_path_rule_shrink is not None:
            result['UserProfilePathRule'] = self.user_profile_path_rule_shrink

        if self.user_profile_rule_type is not None:
            result['UserProfileRuleType'] = self.user_profile_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserProfilePathRule') is not None:
            self.user_profile_path_rule_shrink = m.get('UserProfilePathRule')

        if m.get('UserProfileRuleType') is not None:
            self.user_profile_rule_type = m.get('UserProfileRuleType')

        return self

