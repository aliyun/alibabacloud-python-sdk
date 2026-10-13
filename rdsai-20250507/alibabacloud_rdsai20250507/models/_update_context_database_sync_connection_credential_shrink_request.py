# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContextDatabaseSyncConnectionCredentialShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_id: str = None,
        credentials_shrink: str = None,
        workspace_id: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.connection_id = connection_id
        # This parameter is required.
        self.credentials_shrink = credentials_shrink
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

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.credentials_shrink is not None:
            result['Credentials'] = self.credentials_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('Credentials') is not None:
            self.credentials_shrink = m.get('Credentials')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

