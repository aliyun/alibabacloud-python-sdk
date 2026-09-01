# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataAgentSkillMetaRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        skill_name: str = None,
        upload_location: str = None,
        workspace_id: str = None,
    ):
        # The skill description.
        # - By default, this parameter is optional. The backend parses the ZIP package specified by UploadLocation to obtain the skill description.
        self.description = description
        # The skill name.
        # - By default, this parameter is optional. The backend parses the ZIP package specified by UploadLocation to obtain the skill name.
        self.skill_name = skill_name
        # The full path for uploading the skill ZIP file.
        # - Format: The UploadDir field returned by the DescribeSkillFileUploadSignature operation concatenated with the file name.
        # - Example: ${UploadDir}/${Filename}
        self.upload_location = upload_location
        # The workspace ID.
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

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.upload_location is not None:
            result['UploadLocation'] = self.upload_location

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('UploadLocation') is not None:
            self.upload_location = m.get('UploadLocation')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

