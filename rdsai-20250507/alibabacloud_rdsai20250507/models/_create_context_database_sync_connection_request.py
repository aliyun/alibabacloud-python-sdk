# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContextDatabaseSyncConnectionRequest(DaraModel):
    def __init__(
        self,
        auth_kind: str = None,
        client_token: str = None,
        display_name: str = None,
        plugin_id: str = None,
        workspace_id: str = None,
    ):
        # The authorization method. Valid values: app, pasted-url, static-secret, and none.
        # 
        # This parameter is required.
        self.auth_kind = auth_kind
        # The idempotency token.
        self.client_token = client_token
        # The display name.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The plugin ID.
        # 
        # This parameter is required.
        self.plugin_id = plugin_id
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
        if self.auth_kind is not None:
            result['AuthKind'] = self.auth_kind

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKind') is not None:
            self.auth_kind = m.get('AuthKind')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

