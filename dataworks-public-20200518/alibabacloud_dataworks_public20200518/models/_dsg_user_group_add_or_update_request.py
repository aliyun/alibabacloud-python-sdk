# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgUserGroupAddOrUpdateRequest(DaraModel):
    def __init__(
        self,
        user_groups: List[main_models.DsgUserGroupAddOrUpdateRequestUserGroups] = None,
    ):
        # The information about the user group.
        # 
        # This parameter is required.
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for v1 in self.user_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k1 in self.user_groups:
                result['UserGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k1 in m.get('UserGroups'):
                temp_model = main_models.DsgUserGroupAddOrUpdateRequestUserGroups()
                self.user_groups.append(temp_model.from_map(k1))

        return self

class DsgUserGroupAddOrUpdateRequestUserGroups(DaraModel):
    def __init__(
        self,
        accounts: List[str] = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        project_name: str = None,
        user_group_type: int = None,
        projects: str = None,
    ):
        # The users in the group.
        # 
        # *   If a user group is created by using an Alibaba Cloud account and a RAM role, you can call the [DsgUserGroupQueryUserList](https://help.aliyun.com/document_detail/2786445.html) operation to query the users in the group.
        # *   If a user group is created by using a MaxCompute role, you can call the [DsgUserGroupQueryUserList](https://help.aliyun.com/document_detail/2785695.html) operation to query the users in the group.
        self.accounts = accounts
        # The user group ID.
        # 
        # *   If you do not configure this parameter, the current operation is to add a user group.
        # *   If you configure this parameter, the current operation is to modify a user group. You can call the [DsgUserGroupQueryList](https://help.aliyun.com/document_detail/2786441.html) operation to query the user group ID.
        self.id = id
        # The name of the user group.
        # 
        # This parameter is required.
        self.name = name
        # The owner of the user group.
        # 
        # This parameter is required.
        self.owner = owner
        # The name of the MaxCompute project. You must configure this parameter when you create a MaxCompute user group.
        self.project_name = project_name
        # The type of the user group. Valid values:
        # 
        # *   1: Alibaba Cloud account
        # *   2: RAM role
        # *   3: MaxCompute role
        # 
        # This parameter is required.
        self.user_group_type = user_group_type
        self.projects = projects

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts is not None:
            result['Accounts'] = self.accounts

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type

        if self.projects is not None:
            result['projects'] = self.projects

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            self.accounts = m.get('Accounts')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')

        if m.get('projects') is not None:
            self.projects = m.get('projects')

        return self

