# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContextDatabaseSyncSourceSelectionShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        selected_node_keys_shrink: str = None,
        selection_policy: str = None,
        source_id: str = None,
        workspace_id: str = None,
    ):
        # The idempotency token.
        self.client_token = client_token
        # The list of selected node identifiers.
        # 
        # This parameter is required.
        self.selected_node_keys_shrink = selected_node_keys_shrink
        # The selection policy.
        self.selection_policy = selection_policy
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.selected_node_keys_shrink is not None:
            result['SelectedNodeKeys'] = self.selected_node_keys_shrink

        if self.selection_policy is not None:
            result['SelectionPolicy'] = self.selection_policy

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('SelectedNodeKeys') is not None:
            self.selected_node_keys_shrink = m.get('SelectedNodeKeys')

        if m.get('SelectionPolicy') is not None:
            self.selection_policy = m.get('SelectionPolicy')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

