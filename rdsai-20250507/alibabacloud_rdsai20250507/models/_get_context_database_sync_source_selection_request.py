# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetContextDatabaseSyncSourceSelectionRequest(DaraModel):
    def __init__(
        self,
        source_id: str = None,
        workspace_id: str = None,
    ):
        # The data source ID, which is a system-generated UUID.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The workspace ID.
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
        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

