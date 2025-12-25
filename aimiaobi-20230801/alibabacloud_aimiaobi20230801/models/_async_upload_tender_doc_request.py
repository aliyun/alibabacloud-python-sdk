# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncUploadTenderDocRequest(DaraModel):
    def __init__(
        self,
        file_key: str = None,
        tender_doc_name: str = None,
        workspace_id: str = None,
    ):
        self.file_key = file_key
        self.tender_doc_name = tender_doc_name
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

        if self.tender_doc_name is not None:
            result['TenderDocName'] = self.tender_doc_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('TenderDocName') is not None:
            self.tender_doc_name = m.get('TenderDocName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

