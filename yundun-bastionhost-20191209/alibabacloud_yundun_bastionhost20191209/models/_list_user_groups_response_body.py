# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListUserGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        user_groups: List[main_models.ListUserGroupsResponseBodyUserGroups] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of user groups returned.
        self.total_count = total_count
        # The user groups returned.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserGroups'] = []
        if self.user_groups is not None:
            for k1 in self.user_groups:
                result['UserGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k1 in m.get('UserGroups'):
                temp_model = main_models.ListUserGroupsResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k1))

        return self

class ListUserGroupsResponseBodyUserGroups(DaraModel):
    def __init__(
        self,
        comment: str = None,
        member_count: int = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The description of the user group.
        self.comment = comment
        # The number of users in the user group.
        self.member_count = member_count
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

        if self.member_count is not None:
            result['MemberCount'] = self.member_count

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

