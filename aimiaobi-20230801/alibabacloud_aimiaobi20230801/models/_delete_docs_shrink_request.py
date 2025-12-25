# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDocsShrinkRequest(DaraModel):
    def __init__(
        self,
        doc_ids_shrink: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.doc_ids_shrink = doc_ids_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_ids_shrink is not None:
            result['DocIds'] = self.doc_ids_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocIds') is not None:
            self.doc_ids_shrink = m.get('DocIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

