# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSkillShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        dbtypes_shrink: str = None,
        description: str = None,
        name: str = None,
        skill_id: str = None,
        update_note: str = None,
        upload_id: str = None,
        upload_token: str = None,
        workspace_id: str = None,
    ):
        # The content.
        self.content_shrink = content_shrink
        # The list of database types.
        self.dbtypes_shrink = dbtypes_shrink
        # The description of the Skill. The description can be up to 1000 characters in length.
        self.description = description
        # The name of the Skill. The name can contain only lowercase letters, digits, and hyphens.
        self.name = name
        # The unique identifier of the Skill.
        # 
        # This parameter is required.
        self.skill_id = skill_id
        # The version update note for the ContextDB Skill. Specify this parameter when confirming storage after the check passes. The note can be up to 1000 characters in length.
        self.update_note = update_note
        # The upload session ID returned by GetUploadPolicy for ContextDB full package updates. This parameter is not required for original RDS field updates.
        self.upload_id = upload_id
        # The upload session token paired with UploadId, used to verify ownership. This parameter is not required for original RDS field updates.
        self.upload_token = upload_token
        # The ContextDB workspace ID. This parameter is not required for regular Skill calls.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.dbtypes_shrink is not None:
            result['Dbtypes'] = self.dbtypes_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.update_note is not None:
            result['UpdateNote'] = self.update_note

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
            self.content_shrink = m.get('Content')

        if m.get('Dbtypes') is not None:
            self.dbtypes_shrink = m.get('Dbtypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('UpdateNote') is not None:
            self.update_note = m.get('UpdateNote')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        if m.get('UploadToken') is not None:
            self.upload_token = m.get('UploadToken')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

