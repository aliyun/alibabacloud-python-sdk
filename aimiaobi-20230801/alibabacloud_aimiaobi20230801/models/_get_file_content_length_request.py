# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFileContentLengthRequest(DaraModel):
    def __init__(
        self,
        doc_name: str = None,
        file_url: str = None,
        workspace_id: str = None,
    ):
        self.doc_name = doc_name
        self.file_url = file_url
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

