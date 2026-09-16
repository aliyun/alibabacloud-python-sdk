# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class CreateSkillRequest(DaraModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        dbtypes: List[str] = None,
        description: str = None,
        name: str = None,
        upload_id: str = None,
        upload_token: str = None,
        workspace_id: str = None,
    ):
        # The content.
        self.content = content
        # The list of database types.
        self.dbtypes = dbtypes
        # The Skill description. The description can be up to 1000 characters in length.
        self.description = description
        # The Skill name. The name can contain only lowercase letters, digits, and hyphens.
        self.name = name
        # The Skill upload session ID.
        self.upload_id = upload_id
        # The Skill upload session token.
        self.upload_token = upload_token
        # The ContextDB workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.dbtypes is not None:
            result['Dbtypes'] = self.dbtypes

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        if self.upload_token is not None:
            result['UploadToken'] = self.upload_token

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Dbtypes') is not None:
            self.dbtypes = m.get('Dbtypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        if m.get('UploadToken') is not None:
            self.upload_token = m.get('UploadToken')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

