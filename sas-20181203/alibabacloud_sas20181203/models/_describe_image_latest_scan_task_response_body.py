# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageLatestScanTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task: List[main_models.DescribeImageLatestScanTaskResponseBodyTask] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the information about the task.
        self.task = task

    def validate(self):
        if self.task:
            for v1 in self.task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Task'] = []
        if self.task is not None:
            for k1 in self.task:
                result['Task'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task = []
        if m.get('Task') is not None:
            for k1 in m.get('Task'):
                temp_model = main_models.DescribeImageLatestScanTaskResponseBodyTask()
                self.task.append(temp_model.from_map(k1))

        return self

class DescribeImageLatestScanTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        create: str = None,
        finish: int = None,
        finish_time: int = None,
        id: int = None,
        modified: str = None,
        name: str = None,
        source: str = None,
        start_time: int = None,
        status: str = None,
        target: str = None,
        target_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The time when the task was created. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.create = create
        # The number of images that are scanned.
        self.finish = finish
        # The end time of the task. A value is returned only when the task is in the Finished state. Otherwise, the returned value is empty.
        self.finish_time = finish_time
        # The task ID.
        self.id = id
        # The time when the task was last modified. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.modified = modified
        # The name of the task.
        self.name = name
        # The method in which the task was created. A task can be created in the Security Center console or by calling an API operation. Valid values:
        # 
        # *   **console_batch**: The task was created in the Security Center console.
        # *   **openapi**: The task was created by calling an API operation.
        self.source = source
        # The start time of the task.
        self.start_time = start_time
        # The status of the task. Valid value:
        # 
        # *   **PROCESSING**: The task is running.
        # *   **START**: The task is being started.
        # *   **MESSAGE_SEND**: The scan task is sent.
        # *   **PRE_ANALYZER**: The image is in precheck.
        # *   **SUCCESS**: The task was successful.
        # *   **FAIL**: The task failed.
        # *   **TIMOUT**: The task timed out.
        self.status = status
        # The digest value of the image.
        self.target = target
        # The type of the scanned asset. Valid value:
        # 
        # *   **IMAGE**
        self.target_type = target_type
        # The ID of the scan task.
        self.task_id = task_id
        # The type of the task. Valid value:
        # 
        # *   **IMAGE_SCAN**
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create is not None:
            result['Create'] = self.create

        if self.finish is not None:
            result['Finish'] = self.finish

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modified is not None:
            result['Modified'] = self.modified

        if self.name is not None:
            result['Name'] = self.name

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Create') is not None:
            self.create = m.get('Create')

        if m.get('Finish') is not None:
            self.finish = m.get('Finish')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Modified') is not None:
            self.modified = m.get('Modified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

