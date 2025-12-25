# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class AddLhMembersRequest(DaraModel):
    def __init__(
        self,
        members: List[main_models.AddLhMembersRequestMembers] = None,
        object_id: int = None,
        object_type: int = None,
        tid: int = None,
    ):
        # The information about the users to be added.
        # 
        # This parameter is required.
        self.members = members
        # The ID of the object.
        # 
        # *   If the object is a workspace, you can call the [GetLhSpaceByName](https://help.aliyun.com/document_detail/424379.html) operation to obtain the workspace ID.
        # *   If the object is a task flow, you can call the [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to obtain the task flow ID.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The type of the object. Valid values:
        # 
        # *   **0**: workspace
        # *   **1**: task flow
        # 
        # This parameter is required.
        self.object_type = object_type
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.AddLhMembersRequestMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class AddLhMembersRequestMembers(DaraModel):
    def __init__(
        self,
        roles: List[str] = None,
        user_id: int = None,
    ):
        # The role. Valid values:
        # 
        # *   **ADMIN**: workspace administrator. You can add a workspace administrator only as a DMS administrator or a DBA.
        # *   **MEMBER**: workspace member.
        # *   **DEVELOPER**: task flow developer. Only a workspace member can be added as a task flow developer.
        # 
        # This parameter is required.
        self.roles = roles
        # The ID of the user to be added. You can call the [ListUsers](https://help.aliyun.com/document_detail/141938.html) or [GetUser](https://help.aliyun.com/document_detail/147098.html) operation to obtain the user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.roles is not None:
            result['Roles'] = self.roles

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

