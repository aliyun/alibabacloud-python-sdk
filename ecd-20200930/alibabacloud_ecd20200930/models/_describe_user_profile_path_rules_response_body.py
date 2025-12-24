# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeUserProfilePathRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_profile_path_rule: main_models.DescribeUserProfilePathRulesResponseBodyUserProfilePathRule = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The directory blacklist and whitelist.
        self.user_profile_path_rule = user_profile_path_rule

    def validate(self):
        if self.user_profile_path_rule:
            self.user_profile_path_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_profile_path_rule is not None:
            result['UserProfilePathRule'] = self.user_profile_path_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserProfilePathRule') is not None:
            temp_model = main_models.DescribeUserProfilePathRulesResponseBodyUserProfilePathRule()
            self.user_profile_path_rule = temp_model.from_map(m.get('UserProfilePathRule'))

        return self

class DescribeUserProfilePathRulesResponseBodyUserProfilePathRule(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        rules: List[main_models.DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRules] = None,
        user_profile_rule_type: str = None,
    ):
        # The desktop group ID.
        self.desktop_group_id = desktop_group_id
        # The directory rules.
        self.rules = rules
        # The directory type that is configured for the directory.
        # 
        # Valid values:
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
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.user_profile_rule_type is not None:
            result['UserProfileRuleType'] = self.user_profile_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('UserProfileRuleType') is not None:
            self.user_profile_rule_type = m.get('UserProfileRuleType')

        return self

class DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRules(DaraModel):
    def __init__(
        self,
        black_path: main_models.DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRulesBlackPath = None,
        white_paths: List[main_models.DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRulesWhitePaths] = None,
    ):
        # The blacklist that is configured.
        self.black_path = black_path
        # The directories in the whitelist.
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
            temp_model = main_models.DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRulesBlackPath()
            self.black_path = temp_model.from_map(m.get('BlackPath'))

        self.white_paths = []
        if m.get('WhitePaths') is not None:
            for k1 in m.get('WhitePaths'):
                temp_model = main_models.DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRulesWhitePaths()
                self.white_paths.append(temp_model.from_map(k1))

        return self

class DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRulesWhitePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The path.
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

class DescribeUserProfilePathRulesResponseBodyUserProfilePathRuleRulesBlackPath(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The path.
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

