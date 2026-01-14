# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryUserGroupMemberResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.QueryUserGroupMemberResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # The result of the request for the user group member list.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryUserGroupMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryUserGroupMemberResponseBodyResult(DaraModel):
    def __init__(
        self,
        id: str = None,
        is_user_group: bool = None,
        name: str = None,
        parent_user_group_id: str = None,
        parent_user_group_name: str = None,
    ):
        # ID of the user group or the user group member.
        self.id = id
        # Indicates whether it is a user group. Possible values:
        # 
        # - true: It is a user group.
        # - false: It is a user.
        self.is_user_group = is_user_group
        # Name or nickname of the user group or its member.
        self.name = name
        # ID of the parent user group.
        self.parent_user_group_id = parent_user_group_id
        # Name of the parent user group.
        self.parent_user_group_name = parent_user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.is_user_group is not None:
            result['IsUserGroup'] = self.is_user_group

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id

        if self.parent_user_group_name is not None:
            result['ParentUserGroupName'] = self.parent_user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsUserGroup') is not None:
            self.is_user_group = m.get('IsUserGroup')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')

        if m.get('ParentUserGroupName') is not None:
            self.parent_user_group_name = m.get('ParentUserGroupName')

        return self

