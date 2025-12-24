# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class SetUserProfilePathRulesRequest(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        region_id: str = None,
        user_profile_path_rule: List[main_models.SetUserProfilePathRulesRequestUserProfilePathRule] = None,
        user_profile_rule_type: str = None,
    ):
        # The desktop group ID.
        self.desktop_group_id = desktop_group_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The directories that you want to configure in the blacklist and whitelist.
        self.user_profile_path_rule = user_profile_path_rule
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
        if self.user_profile_path_rule:
            for v1 in self.user_profile_path_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['UserProfilePathRule'] = []
        if self.user_profile_path_rule is not None:
            for k1 in self.user_profile_path_rule:
                result['UserProfilePathRule'].append(k1.to_map() if k1 else None)

        if self.user_profile_rule_type is not None:
            result['UserProfileRuleType'] = self.user_profile_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.user_profile_path_rule = []
        if m.get('UserProfilePathRule') is not None:
            for k1 in m.get('UserProfilePathRule'):
                temp_model = main_models.SetUserProfilePathRulesRequestUserProfilePathRule()
                self.user_profile_path_rule.append(temp_model.from_map(k1))

        if m.get('UserProfileRuleType') is not None:
            self.user_profile_rule_type = m.get('UserProfileRuleType')

        return self

class SetUserProfilePathRulesRequestUserProfilePathRule(DaraModel):
    def __init__(
        self,
        black_path: main_models.SetUserProfilePathRulesRequestUserProfilePathRuleBlackPath = None,
        white_paths: List[main_models.SetUserProfilePathRulesRequestUserProfilePathRuleWhitePaths] = None,
    ):
        # The directory in the blacklist.
        self.black_path = black_path
        # The directories that you want to configure in the whitelist.
        self.white_paths = white_paths

    def validate(self):
        if self.black_path:
            self.black_path.validate()
        if self.white_paths:
            for v1 in self.white_paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_path is not None:
            result['BlackPath'] = self.black_path.to_map()

        result['WhitePaths'] = []
        if self.white_paths is not None:
            for k1 in self.white_paths:
                result['WhitePaths'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackPath') is not None:
            temp_model = main_models.SetUserProfilePathRulesRequestUserProfilePathRuleBlackPath()
            self.black_path = temp_model.from_map(m.get('BlackPath'))

        self.white_paths = []
        if m.get('WhitePaths') is not None:
            for k1 in m.get('WhitePaths'):
                temp_model = main_models.SetUserProfilePathRulesRequestUserProfilePathRuleWhitePaths()
                self.white_paths.append(temp_model.from_map(k1))

        return self

class SetUserProfilePathRulesRequestUserProfilePathRuleWhitePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The whitelist path.
        self.path = path
        # The path type.
        # 
        # Valid values:
        # 
        # *   file
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   folder
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SetUserProfilePathRulesRequestUserProfilePathRuleBlackPath(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The blacklist path.
        self.path = path
        # The path type.
        # 
        # Valid values:
        # 
        # *   file
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   folder
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

