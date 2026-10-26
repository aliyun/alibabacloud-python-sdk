# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListUserGroupsForUserResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        request_id: str = None,
        user_groups: List[main_models.ListUserGroupsForUserResponseBodyUserGroups] = None,
    ):
        # The total number of user groups returned.
        self.count = count
        # The request ID.
        self.request_id = request_id
        # The list of user groups.
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
        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserGroups'] = []
        if self.user_groups is not None:
            for k1 in self.user_groups:
                result['UserGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k1 in m.get('UserGroups'):
                temp_model = main_models.ListUserGroupsForUserResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k1))

        return self

class ListUserGroupsForUserResponseBodyUserGroups(DaraModel):
    def __init__(
        self,
        comment: str = None,
        project_id: str = None,
        project_name: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The remarks of the user group.
        self.comment = comment
        # The ID of the project to which the user group belongs.
        self.project_id = project_id
        # The name of the project to which the user group belongs.
        self.project_name = project_name
        # The ID of the user group.
        self.user_group_id = user_group_id
        # The name of the user group.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

