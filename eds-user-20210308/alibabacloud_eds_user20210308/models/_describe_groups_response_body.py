# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        groups: List[main_models.DescribeGroupsResponseBodyGroups] = None,
        request_id: str = None,
    ):
        # The number of the entries returned.
        self.count = count
        # The user groups.
        self.groups = groups
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGroupsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        attached_login_policy: main_models.DescribeGroupsResponseBodyGroupsAttachedLoginPolicy = None,
        authed_resources: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        transfer_file_need_approval: bool = None,
        user_count: int = None,
    ):
        self.attached_login_policy = attached_login_policy
        # The type of the resource assigned to the user group.
        self.authed_resources = authed_resources
        # The time when the user group is created.
        self.create_time = create_time
        # The description of the user group.
        self.description = description
        self.group_id = group_id
        # The name of the user group.
        self.group_name = group_name
        # Indicates whether the file approval feature is enabled.
        self.transfer_file_need_approval = transfer_file_need_approval
        # The number of users in the user group.
        self.user_count = user_count

    def validate(self):
        if self.attached_login_policy:
            self.attached_login_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_login_policy is not None:
            result['AttachedLoginPolicy'] = self.attached_login_policy.to_map()

        if self.authed_resources is not None:
            result['AuthedResources'] = self.authed_resources

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.transfer_file_need_approval is not None:
            result['TransferFileNeedApproval'] = self.transfer_file_need_approval

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedLoginPolicy') is not None:
            temp_model = main_models.DescribeGroupsResponseBodyGroupsAttachedLoginPolicy()
            self.attached_login_policy = temp_model.from_map(m.get('AttachedLoginPolicy'))

        if m.get('AuthedResources') is not None:
            self.authed_resources = m.get('AuthedResources')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('TransferFileNeedApproval') is not None:
            self.transfer_file_need_approval = m.get('TransferFileNeedApproval')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

class DescribeGroupsResponseBodyGroupsAttachedLoginPolicy(DaraModel):
    def __init__(
        self,
        name: str = None,
        policy_id: str = None,
    ):
        self.name = name
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

