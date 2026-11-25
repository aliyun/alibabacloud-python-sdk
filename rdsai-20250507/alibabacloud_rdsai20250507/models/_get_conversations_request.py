# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConversationsRequest(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        last_id: str = None,
        limit: str = None,
        pinned: str = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        # The ID of the flow.
        self.flow_id = flow_id
        # The ID of the last conversation record.
        self.last_id = last_id
        # The paging Settings for the number of entries per page in a paged query. Valid values: 1 to 100.
        self.limit = limit
        # The pin mark for application favorites.
        self.pinned = pinned
        # The sorting criterion.
        self.sort_by = sort_by
        # The ID of the ContextDB workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.last_id is not None:
            result['LastId'] = self.last_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.pinned is not None:
            result['Pinned'] = self.pinned

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('LastId') is not None:
            self.last_id = m.get('LastId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

