# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetOptimizeRunResponseBody(DaraModel):
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
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        trajectory_count: int = None,
        trigger_type: str = None,
        type: str = None,
        window_end_time: int = None,
        window_start_time: int = None,
    ):
        self.attempt_count = attempt_count
        self.create_time = create_time
        self.current_stage = current_stage
        self.error_code = error_code
        self.error_message = error_message
        self.extra = extra
        self.finish_time = finish_time
        self.max_attempts = max_attempts
        self.optimize_run_id = optimize_run_id
        self.optimize_task_name = optimize_task_name
        self.progress = progress
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.trajectory_count = trajectory_count
        self.trigger_type = trigger_type
        self.type = type
        self.window_end_time = window_end_time
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

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

