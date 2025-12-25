# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunGenerateQuestionsRequest(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        model_name: str = None,
        reference_content: str = None,
        session_id: str = None,
        workspace_id: str = None,
    ):
        self.doc_id = doc_id
        self.model_name = model_name
        self.reference_content = reference_content
        self.session_id = session_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.reference_content is not None:
            result['ReferenceContent'] = self.reference_content

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ReferenceContent') is not None:
            self.reference_content = m.get('ReferenceContent')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

