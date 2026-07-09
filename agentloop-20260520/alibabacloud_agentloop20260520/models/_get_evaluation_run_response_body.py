# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetEvaluationRunResponseBody(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        data_end_time: int = None,
        data_start_time: int = None,
        evaluator_progress: List[main_models.GetEvaluationRunResponseBodyEvaluatorProgress] = None,
        evaluators: str = None,
        failed_count: int = None,
        request_id: str = None,
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
        # The end time of the data window for the run, in seconds-level UNIX timestamp.
        self.data_end_time = data_end_time
        # The start time of the data window for the run, in seconds-level UNIX timestamp.
        self.data_start_time = data_start_time
        # The list of progress details by evaluator.
        self.evaluator_progress = evaluator_progress
        # The evaluator configuration snapshot at the time the run was created, in JSON string format.
        self.evaluators = evaluators
        # The number of failed entries.
        self.failed_count = failed_count
        # The request ID.
        self.request_id = request_id
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
        if self.evaluator_progress:
            for v1 in self.evaluator_progress:
                 if v1:
                    v1.validate()

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

        result['evaluatorProgress'] = []
        if self.evaluator_progress is not None:
            for k1 in self.evaluator_progress:
                result['evaluatorProgress'].append(k1.to_map() if k1 else None)

        if self.evaluators is not None:
            result['evaluators'] = self.evaluators

        if self.failed_count is not None:
            result['failedCount'] = self.failed_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        self.evaluator_progress = []
        if m.get('evaluatorProgress') is not None:
            for k1 in m.get('evaluatorProgress'):
                temp_model = main_models.GetEvaluationRunResponseBodyEvaluatorProgress()
                self.evaluator_progress.append(temp_model.from_map(k1))

        if m.get('evaluators') is not None:
            self.evaluators = m.get('evaluators')

        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

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

class GetEvaluationRunResponseBodyEvaluatorProgress(DaraModel):
    def __init__(
        self,
        evaluator_name: str = None,
        failed_count: int = None,
        success_count: int = None,
        total_count: int = None,
    ):
        # The evaluator name.
        self.evaluator_name = evaluator_name
        # The number of failed entries for this evaluator.
        self.failed_count = failed_count
        # The number of successful entries for this evaluator.
        self.success_count = success_count
        # The total number of entries for this evaluator.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluator_name is not None:
            result['evaluatorName'] = self.evaluator_name

        if self.failed_count is not None:
            result['failedCount'] = self.failed_count

        if self.success_count is not None:
            result['successCount'] = self.success_count

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('evaluatorName') is not None:
            self.evaluator_name = m.get('evaluatorName')

        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

