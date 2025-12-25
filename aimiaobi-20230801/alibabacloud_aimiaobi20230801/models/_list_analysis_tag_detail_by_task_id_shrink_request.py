# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAnalysisTagDetailByTaskIdShrinkRequest(DaraModel):
    def __init__(
        self,
        categories_shrink: str = None,
        current: int = None,
        max_results: int = None,
        next_token: str = None,
        size: int = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        self.categories_shrink = categories_shrink
        self.current = current
        self.max_results = max_results
        self.next_token = next_token
        self.size = size
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories_shrink is not None:
            result['Categories'] = self.categories_shrink

        if self.current is not None:
            result['Current'] = self.current

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.size is not None:
            result['Size'] = self.size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories_shrink = m.get('Categories')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

