# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContextDatabaseMemberRequest(DaraModel):
    def __init__(
        self,
        member_id: str = None,
        role: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The member ID.
        # 
        # This parameter is required.
        self.member_id = member_id
        # The new role. Valid values: owner, admin, and member. If not specified, the current role is retained.
        self.role = role
        # The new status. Valid values: active, disabled, and deleted. If not specified, the current status is retained.
        self.status = status
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

