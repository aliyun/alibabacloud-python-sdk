# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListOptimizeRunsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        optimize_runs: List[main_models.ListOptimizeRunsResponseBodyOptimizeRuns] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # The token for the next page.
        self.next_token = next_token
        # The list of run instances.
        self.optimize_runs = optimize_runs
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.optimize_runs:
            for v1 in self.optimize_runs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['optimizeRuns'] = []
        if self.optimize_runs is not None:
            for k1 in self.optimize_runs:
                result['optimizeRuns'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.optimize_runs = []
        if m.get('optimizeRuns') is not None:
            for k1 in m.get('optimizeRuns'):
                temp_model = main_models.ListOptimizeRunsResponseBodyOptimizeRuns()
                self.optimize_runs.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListOptimizeRunsResponseBodyOptimizeRuns(DaraModel):
    def __init__(
        self,
        attempt_count: int = None,
        create_time: str = None,
        current_stage: str = None,
        error_code: str = None,
        error_message: str = None,
        extra: Dict[str, Any] = None,
        finish_time: str = None,
        max_attempts: int = None,
        optimize_run_id: str = None,
        optimize_task_name: str = None,
        progress: Dict[str, Any] = None,
        start_time: str = None,
        status: str = None,
        trajectory_count: int = None,
        trigger_type: str = None,
        type: str = None,
        window_end_time: int = None,
        window_start_time: int = None,
    ):
        # The number of executed attempts.
        self.attempt_count = attempt_count
        # The creation time.
        self.create_time = create_time
        # The current execution stage.
        self.current_stage = current_stage
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The execution summary and finite-state information. To obtain complete result references, frozen outputs, and publish receipts, call GetOptimizeRun.
        self.extra = extra
        # The completion time.
        self.finish_time = finish_time
        # The maximum number of attempts.
        self.max_attempts = max_attempts
        # The ID of the run instance.
        self.optimize_run_id = optimize_run_id
        # The name of the optimization task.
        self.optimize_task_name = optimize_task_name
        # The current execution progress. The fields are defined by the task type.
        self.progress = progress
        # The initial start time.
        self.start_time = start_time
        # The execution status.
        self.status = status
        # The number of analysis trajectories.
        self.trajectory_count = trajectory_count
        # The trigger type.
        self.trigger_type = trigger_type
        # The snapshot of the task type.
        self.type = type
        # The end time of the analysis window in UNIX seconds.
        self.window_end_time = window_end_time
        # The start time of the analysis window in UNIX seconds.
        self.window_start_time = window_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempt_count is not None:
            result['attemptCount'] = self.attempt_count

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.current_stage is not None:
            result['currentStage'] = self.current_stage

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.extra is not None:
            result['extra'] = self.extra

        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.max_attempts is not None:
            result['maxAttempts'] = self.max_attempts

        if self.optimize_run_id is not None:
            result['optimizeRunId'] = self.optimize_run_id

        if self.optimize_task_name is not None:
            result['optimizeTaskName'] = self.optimize_task_name

        if self.progress is not None:
            result['progress'] = self.progress

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.trajectory_count is not None:
            result['trajectoryCount'] = self.trajectory_count

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        if self.type is not None:
            result['type'] = self.type

        if self.window_end_time is not None:
            result['windowEndTime'] = self.window_end_time

        if self.window_start_time is not None:
            result['windowStartTime'] = self.window_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attemptCount') is not None:
            self.attempt_count = m.get('attemptCount')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('currentStage') is not None:
            self.current_stage = m.get('currentStage')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('maxAttempts') is not None:
            self.max_attempts = m.get('maxAttempts')

        if m.get('optimizeRunId') is not None:
            self.optimize_run_id = m.get('optimizeRunId')

        if m.get('optimizeTaskName') is not None:
            self.optimize_task_name = m.get('optimizeTaskName')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('trajectoryCount') is not None:
            self.trajectory_count = m.get('trajectoryCount')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('windowEndTime') is not None:
            self.window_end_time = m.get('windowEndTime')

        if m.get('windowStartTime') is not None:
            self.window_start_time = m.get('windowStartTime')

        return self

