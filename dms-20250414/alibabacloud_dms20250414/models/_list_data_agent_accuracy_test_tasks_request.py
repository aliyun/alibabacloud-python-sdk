# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAgentAccuracyTestTasksRequest(DaraModel):
    def __init__(
        self,
        accuracy_test_ins_id: str = None,
        accuracy_test_task_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: str = None,
        page_size: str = None,
        workspace_id: str = None,
    ):
        # The accuracy test instance ID.
        self.accuracy_test_ins_id = accuracy_test_ins_id
        # The task ID used for exact filtering.
        self.accuracy_test_task_id = accuracy_test_task_id
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accuracy_test_ins_id is not None:
            result['AccuracyTestInsId'] = self.accuracy_test_ins_id

        if self.accuracy_test_task_id is not None:
            result['AccuracyTestTaskId'] = self.accuracy_test_task_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccuracyTestInsId') is not None:
            self.accuracy_test_ins_id = m.get('AccuracyTestInsId')

        if m.get('AccuracyTestTaskId') is not None:
            self.accuracy_test_task_id = m.get('AccuracyTestTaskId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

