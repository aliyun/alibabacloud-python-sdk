# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadDocShrinkRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        docs_shrink: str = None,
        workspace_id: str = None,
    ):
        self.category_id = category_id
        # This parameter is required.
        self.docs_shrink = docs_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.docs_shrink is not None:
            result['Docs'] = self.docs_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Docs') is not None:
            self.docs_shrink = m.get('Docs')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

