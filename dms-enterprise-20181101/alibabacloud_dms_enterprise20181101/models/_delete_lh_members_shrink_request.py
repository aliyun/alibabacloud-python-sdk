# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLhMembersShrinkRequest(DaraModel):
    def __init__(
        self,
        member_ids_shrink: str = None,
        object_id: int = None,
        object_type: int = None,
        tid: int = None,
    ):
        # The ID of the user to be removed. You can call the [ListUsers](https://help.aliyun.com/document_detail/141938.html) or [GetUser](https://help.aliyun.com/document_detail/147098.html) operation to obtain the user ID.
        # 
        # This parameter is required.
        self.member_ids_shrink = member_ids_shrink
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_ids_shrink is not None:
            result['MemberIds'] = self.member_ids_shrink

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberIds') is not None:
            self.member_ids_shrink = m.get('MemberIds')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

