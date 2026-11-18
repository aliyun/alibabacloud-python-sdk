# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DescribeUserProfilePathRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeUserProfilePathRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code returned when the request fails.
        self.code = code
        # The path rules and user profile roaming configurations.
        self.data = data
        # The error message returned when the request fails.
        self.message = message
        # The unique identifier of the request, which can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeUserProfilePathRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserProfilePathRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_set_id: str = None,
        domain_id: str = None,
        file_system_id: str = None,
        profile_follow_switch: bool = None,
        remote_storage_path: str = None,
        rule_type: str = None,
        rules: List[main_models.DescribeUserProfilePathRulesResponseBodyDataRules] = None,
        user_profile_size: int = None,
        user_profile_switch: bool = None,
    ):
        # The app instance group ID corresponding to the rule. When querying set rules, this is the primary app instance group ID.
        self.app_instance_group_id = app_instance_group_id
        # The app instance group set ID corresponding to the rule. This is returned when querying set rules.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The user profile roaming storage domain ID bound to the app instance group. This field may be omitted if no domain is bound.
        self.domain_id = domain_id
        # Not enabled. The current query result does not provide the file system ID. The example is used to illustrate the field status.
        self.file_system_id = file_system_id
        # The user profile roaming switch. A value of `true` indicates that the feature is enabled, and a value of `false` indicates that the feature is disabled.
        self.profile_follow_switch = profile_follow_switch
        # The remote storage path for user profile roaming. If this path is not separately configured for the app instance group, the app instance group ID is returned.
        self.remote_storage_path = remote_storage_path
        # The path rule type. Valid values:
        # - `Default`: Queries system default rules. Both target IDs can be omitted.
        # - `AppInstanceGroup`: Queries the rules of an app instance group or an app instance group set.
        self.rule_type = rule_type
        # The list of user profile roaming path rules.
        self.rules = rules
        # The storage quota for user profile roaming, in GB. This field may be omitted if it is not configured.
        self.user_profile_size = user_profile_size
        # The user profile roaming switch. The value is the same as ProfileFollowSwitch. A value of `true` indicates that the feature is enabled, and a value of `false` indicates that the feature is disabled.
        self.user_profile_switch = user_profile_switch

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
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_set_id is not None:
            result['AppInstanceGroupSetId'] = self.app_instance_group_set_id

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.profile_follow_switch is not None:
            result['ProfileFollowSwitch'] = self.profile_follow_switch

        if self.remote_storage_path is not None:
            result['RemoteStoragePath'] = self.remote_storage_path

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.user_profile_size is not None:
            result['UserProfileSize'] = self.user_profile_size

        if self.user_profile_switch is not None:
            result['UserProfileSwitch'] = self.user_profile_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupSetId') is not None:
            self.app_instance_group_set_id = m.get('AppInstanceGroupSetId')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ProfileFollowSwitch') is not None:
            self.profile_follow_switch = m.get('ProfileFollowSwitch')

        if m.get('RemoteStoragePath') is not None:
            self.remote_storage_path = m.get('RemoteStoragePath')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeUserProfilePathRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('UserProfileSize') is not None:
            self.user_profile_size = m.get('UserProfileSize')

        if m.get('UserProfileSwitch') is not None:
            self.user_profile_switch = m.get('UserProfileSwitch')

        return self

class DescribeUserProfilePathRulesResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        black_path: main_models.DescribeUserProfilePathRulesResponseBodyDataRulesBlackPath = None,
        white_paths: List[main_models.DescribeUserProfilePathRulesResponseBodyDataRulesWhitePaths] = None,
    ):
        # The file or directory excluded from user profile roaming.
        self.black_path = black_path
        # The list of files or directories that still participate in user profile roaming under the excluded directories.
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
            temp_model = main_models.DescribeUserProfilePathRulesResponseBodyDataRulesBlackPath()
            self.black_path = temp_model.from_map(m.get('BlackPath'))

        self.white_paths = []
        if m.get('WhitePaths') is not None:
            for k1 in m.get('WhitePaths'):
                temp_model = main_models.DescribeUserProfilePathRulesResponseBodyDataRulesWhitePaths()
                self.white_paths.append(temp_model.from_map(k1))

        return self

class DescribeUserProfilePathRulesResponseBodyDataRulesWhitePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The exception path relative to BlackPath.Path.
        self.path = path
        # The path type. Valid values:
        # - `file`: File.
        # - `folder`: Folder.
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

class DescribeUserProfilePathRulesResponseBodyDataRulesBlackPath(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The excluded path relative to the user profile directory.
        self.path = path
        # The path type. Valid values:
        # - `file`: File.
        # - `folder`: Folder.
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

