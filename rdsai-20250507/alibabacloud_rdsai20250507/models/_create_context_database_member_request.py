# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContextDatabaseMemberRequest(DaraModel):
    def __init__(
        self,
        generate_initial_key: bool = None,
        initial_key_name: str = None,
        member_name: str = None,
        role: str = None,
        workspace_id: str = None,
    ):
        # Specifies whether to issue the first API key when the member is created. Default value: false.
        self.generate_initial_key = generate_initial_key
        # The name of the first API key. This parameter takes effect only when GenerateInitialKey is set to true.
        self.initial_key_name = initial_key_name
        # The member name.
        # 
        # This parameter is required.
        self.member_name = member_name
        # The member role. Valid values:
        # 
        # - owner
        # - admin
        # - member
        # 
        # This parameter is required.
        self.role = role
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
        if self.generate_initial_key is not None:
            result['GenerateInitialKey'] = self.generate_initial_key

        if self.initial_key_name is not None:
            result['InitialKeyName'] = self.initial_key_name

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.role is not None:
            result['Role'] = self.role

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateInitialKey') is not None:
            self.generate_initial_key = m.get('GenerateInitialKey')

        if m.get('InitialKeyName') is not None:
            self.initial_key_name = m.get('InitialKeyName')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

