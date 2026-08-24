# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContextDatabaseWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        api_key_name: str = None,
        created_at: str = None,
        member_id: str = None,
        member_name: str = None,
        request_id: str = None,
        role: str = None,
        status: str = None,
        type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The plaintext API key. This value is returned only once at creation time. The caller must persist it.
        self.api_key = api_key
        # The name of the first API key. The value is fixed as default.
        self.api_key_name = api_key_name
        # The time when the workspace was created, in ISO 8601 format.
        self.created_at = created_at
        # The ID of the first member.
        self.member_id = member_id
        # The name of the first member.
        self.member_name = member_name
        # The request ID.
        self.request_id = request_id
        # The role of the first member. The value is fixed as owner.
        self.role = role
        # The workspace status. Valid values:
        # - Active: running normally.
        # - Locked: locked due to overdue payment or expiration.
        self.status = status
        # The workspace type. Valid values:
        # - personal: individual account.
        # - enterprise: enterprise account.
        self.type = type
        # The ID of the new workspace.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_key_name is not None:
            result['ApiKeyName'] = self.api_key_name

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiKeyName') is not None:
            self.api_key_name = m.get('ApiKeyName')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

