# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAgentAccuracyTestResultsRequest(DaraModel):
    def __init__(
        self,
        accuracy_test_ins_id: str = None,
        accuracy_test_result_id: str = None,
        accuracy_test_subtask_id: str = None,
        accuracy_test_task_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The instance ID of the accuracy test.
        self.accuracy_test_ins_id = accuracy_test_ins_id
        # The result ID used to retrieve a single record.
        self.accuracy_test_result_id = accuracy_test_result_id
        # The subtask ID used to filter results.
        self.accuracy_test_subtask_id = accuracy_test_subtask_id
        # The ID of the accuracy test task.
        self.accuracy_test_task_id = accuracy_test_task_id
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
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

        if self.accuracy_test_result_id is not None:
            result['AccuracyTestResultId'] = self.accuracy_test_result_id

        if self.accuracy_test_subtask_id is not None:
            result['AccuracyTestSubtaskId'] = self.accuracy_test_subtask_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccuracyTestInsId') is not None:
            self.accuracy_test_ins_id = m.get('AccuracyTestInsId')

        if m.get('AccuracyTestResultId') is not None:
            self.accuracy_test_result_id = m.get('AccuracyTestResultId')

        if m.get('AccuracyTestSubtaskId') is not None:
            self.accuracy_test_subtask_id = m.get('AccuracyTestSubtaskId')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

