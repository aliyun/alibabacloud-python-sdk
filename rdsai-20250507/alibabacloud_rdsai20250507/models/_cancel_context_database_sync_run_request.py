# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelContextDatabaseSyncRunRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        run_id: str = None,
        workspace_id: str = None,
    ):
        # The idempotence token.
        self.client_token = client_token
        # The run ID, a system-generated UUID.
        # 
        # This parameter is required.
        self.run_id = run_id
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

