# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetContextDatabaseUsageRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        workspace_id: str = None,
    ):
        # The end time of the query range, exclusive. It must be later than `StartTime`. Use the ISO 8601 time format, such as `2026-08-01T00:00:00Z` (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start time of the query range, inclusive. Use the ISO 8601 time format, such as `2026-07-01T00:00:00Z` (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the workspace to query. If specified, only the data of this workspace under the caller account is queried. Locked workspaces can also be queried. If omitted, all workspaces under the caller account are queried.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

