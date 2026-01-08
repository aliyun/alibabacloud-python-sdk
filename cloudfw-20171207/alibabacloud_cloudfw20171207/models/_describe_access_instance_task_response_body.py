# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessInstanceTaskResponseBody(DaraModel):
    def __init__(
        self,
        is_found: bool = None,
        request_id: str = None,
        task_finish_timestamp: int = None,
        task_id: str = None,
        task_name: str = None,
        task_start_timestamp: int = None,
        task_status: str = None,
        task_steps: List[main_models.DescribeAccessInstanceTaskResponseBodyTaskSteps] = None,
    ):
        self.is_found = is_found
        self.request_id = request_id
        self.task_finish_timestamp = task_finish_timestamp
        self.task_id = task_id
        self.task_name = task_name
        self.task_start_timestamp = task_start_timestamp
        self.task_status = task_status
        self.task_steps = task_steps

    def validate(self):
        if self.task_steps:
            for v1 in self.task_steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_found is not None:
            result['IsFound'] = self.is_found

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_finish_timestamp is not None:
            result['TaskFinishTimestamp'] = self.task_finish_timestamp

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_start_timestamp is not None:
            result['TaskStartTimestamp'] = self.task_start_timestamp

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        result['TaskSteps'] = []
        if self.task_steps is not None:
            for k1 in self.task_steps:
                result['TaskSteps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsFound') is not None:
            self.is_found = m.get('IsFound')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskFinishTimestamp') is not None:
            self.task_finish_timestamp = m.get('TaskFinishTimestamp')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStartTimestamp') is not None:
            self.task_start_timestamp = m.get('TaskStartTimestamp')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        self.task_steps = []
        if m.get('TaskSteps') is not None:
            for k1 in m.get('TaskSteps'):
                temp_model = main_models.DescribeAccessInstanceTaskResponseBodyTaskSteps()
                self.task_steps.append(temp_model.from_map(k1))

        return self

class DescribeAccessInstanceTaskResponseBodyTaskSteps(DaraModel):
    def __init__(
        self,
        step_name: str = None,
        step_progress: str = None,
        step_status: str = None,
    ):
        self.step_name = step_name
        self.step_progress = step_progress
        self.step_status = step_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.step_progress is not None:
            result['StepProgress'] = self.step_progress

        if self.step_status is not None:
            result['StepStatus'] = self.step_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('StepProgress') is not None:
            self.step_progress = m.get('StepProgress')

        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')

        return self

