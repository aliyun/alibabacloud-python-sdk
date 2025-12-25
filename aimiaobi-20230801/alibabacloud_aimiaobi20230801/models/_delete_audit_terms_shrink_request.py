# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAuditTermsShrinkRequest(DaraModel):
    def __init__(
        self,
        id_list_shrink: str = None,
        workspace_id: str = None,
    ):
        self.id_list_shrink = id_list_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id_list_shrink is not None:
            result['IdList'] = self.id_list_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdList') is not None:
            self.id_list_shrink = m.get('IdList')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

