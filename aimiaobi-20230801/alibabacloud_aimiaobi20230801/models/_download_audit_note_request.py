# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadAuditNoteRequest(DaraModel):
    def __init__(
        self,
        note_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # Rule library ID. If left blank, the default is Default.
        self.note_id = note_id
        # The task ID obtained by calling the SubmitAuditNote API. This is the unique identifier for the custom rule library task index. Store it securely when using it. When using this API, if the input parameters include \\`taskId\\`, you can retrieve the structured rule library that you successfully uploaded via the SubmitAuditNote API but has not undergone post-processing by ConfirmAndProcessAuditNote. If the input parameters do not include \\`taskId\\`, you can retrieve the structured rule library that has undergone post-processing and is available for auditing.
        self.task_id = task_id
        # The unique identifier of the Alibaba Cloud Model Studio workspace. Get the [Workspace ID](https://help.aliyun.com/document_detail/2782167.html).
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
        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

