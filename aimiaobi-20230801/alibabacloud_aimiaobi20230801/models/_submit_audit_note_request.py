# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAuditNoteRequest(DaraModel):
    def __init__(
        self,
        file_key: str = None,
        note_id: str = None,
        workspace_id: str = None,
    ):
        # The FileKey of your rule library file stored in Alibaba Cloud OSS. For how to generate a FileKey, see [Common APIs: GenerateUploadConfig for File Upload and Download](https://next.api.aliyun.com/document/AiMiaoBi/2023-08-01/GenerateUploadConfig?spm=openapi-amp.newDocPublishment.0.0.18fc281fOiiBil). Your rule library file must be in DOCX, XLSX, or PDF format. If you use XLSX, it must have exactly two columns. The table header must be "Proofreading Basis" and "Source". XLSX files give the best parsing results. DOCX and PDF files are also parsed automatically.
        # 
        # This parameter is required.
        self.file_key = file_key
        # ID of the rule library. If you omit this parameter, the system uses Default.
        self.note_id = note_id
        # Unique identifier of your Model Studio workspace. To get this ID, see [Get the Workspace ID](https://help.aliyun.com/document_detail/2782167.html).
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
        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

