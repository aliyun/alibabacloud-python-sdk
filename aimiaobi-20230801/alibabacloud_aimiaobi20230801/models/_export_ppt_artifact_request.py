# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportPptArtifactRequest(DaraModel):
    def __init__(
        self,
        edit: bool = None,
        export_file_type: str = None,
        ppt_artifact_id: int = None,
        workspace_id: str = None,
        zip: bool = None,
    ):
        self.edit = edit
        self.export_file_type = export_file_type
        # This parameter is required.
        self.ppt_artifact_id = ppt_artifact_id
        self.workspace_id = workspace_id
        self.zip = zip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edit is not None:
            result['Edit'] = self.edit

        if self.export_file_type is not None:
            result['ExportFileType'] = self.export_file_type

        if self.ppt_artifact_id is not None:
            result['PptArtifactId'] = self.ppt_artifact_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.zip is not None:
            result['Zip'] = self.zip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edit') is not None:
            self.edit = m.get('Edit')

        if m.get('ExportFileType') is not None:
            self.export_file_type = m.get('ExportFileType')

        if m.get('PptArtifactId') is not None:
            self.ppt_artifact_id = m.get('PptArtifactId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('Zip') is not None:
            self.zip = m.get('Zip')

        return self

