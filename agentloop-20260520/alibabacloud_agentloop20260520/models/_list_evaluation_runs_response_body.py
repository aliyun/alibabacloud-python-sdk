# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListEvaluationRunsResponseBody(DaraModel):
    def __init__(
        self,
        evaluation_runs: List[main_models.ListEvaluationRunsResponseBodyEvaluationRuns] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of run summaries.
        self.evaluation_runs = evaluation_runs
        # The number of entries per page used in this request.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that no more pages exist.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of runs that match the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.evaluation_runs:
            for v1 in self.evaluation_runs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['evaluationRuns'] = []
        if self.evaluation_runs is not None:
            for k1 in self.evaluation_runs:
                result['evaluationRuns'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_runs = []
        if m.get('evaluationRuns') is not None:
            for k1 in m.get('evaluationRuns'):
                temp_model = main_models.ListEvaluationRunsResponseBodyEvaluationRuns()
                self.evaluation_runs.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListEvaluationRunsResponseBodyEvaluationRuns(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        data_end_time: int = None,
        data_start_time: int = None,
        failed_count: int = None,
        run_id: str = None,
        run_name: str = None,
        run_type: str = None,
        status: str = None,
        success_count: int = None,
        task_id: str = None,
        total_count: int = None,
        updated_at: int = None,
    ):
        # The creation time, in seconds-level UNIX timestamp.
        self.created_at = created_at
        # The end time of the data window for this run, in seconds-level UNIX timestamp.
        self.data_end_time = data_end_time
        # The start time of the data window for this run, in seconds-level UNIX timestamp.
        self.data_start_time = data_start_time
        # The number of failed entries.
        self.failed_count = failed_count
        # The run ID.
        self.run_id = run_id
        # The run name.
        self.run_name = run_name
        # The run type.
        self.run_type = run_type
        # The run status.
        self.status = status
        # The number of successful entries.
        self.success_count = success_count
        # The evaluation task ID.
        self.task_id = task_id
        # The total number of evaluation entries.
        self.total_count = total_count
        # The update time, in seconds-level UNIX timestamp.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.data_end_time is not None:
            result['dataEndTime'] = self.data_end_time

        if self.data_start_time is not None:
            result['dataStartTime'] = self.data_start_time

        if self.failed_count is not None:
            result['failedCount'] = self.failed_count

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.run_name is not None:
            result['runName'] = self.run_name

        if self.run_type is not None:
            result['runType'] = self.run_type

        if self.status is not None:
            result['status'] = self.status

        if self.success_count is not None:
            result['successCount'] = self.success_count

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('dataEndTime') is not None:
            self.data_end_time = m.get('dataEndTime')

        if m.get('dataStartTime') is not None:
            self.data_start_time = m.get('dataStartTime')

        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('runName') is not None:
            self.run_name = m.get('runName')

        if m.get('runType') is not None:
            self.run_type = m.get('runType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

