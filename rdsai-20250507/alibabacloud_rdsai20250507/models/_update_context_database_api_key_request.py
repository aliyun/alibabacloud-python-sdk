# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContextDatabaseApiKeyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        key_id: int = None,
        member_id: str = None,
        name: str = None,
        workspace_id: str = None,
    ):
        # The new description.
        self.description = description
        # API Key ID
        # 
        # This parameter is required.
        self.key_id = key_id
        # The member ID.
        # 
        # This parameter is required.
        self.member_id = member_id
        # The new display name.
        self.name = name
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
        if self.description is not None:
            result['Description'] = self.description

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.name is not None:
            result['Name'] = self.name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

