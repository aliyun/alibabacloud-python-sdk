# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPptArtifactExportResultRequest(DaraModel):
    def __init__(
        self,
        export_task_id: str = None,
        workspace_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

