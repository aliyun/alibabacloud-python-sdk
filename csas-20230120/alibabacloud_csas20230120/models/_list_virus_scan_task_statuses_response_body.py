# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListVirusScanTaskStatusesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.ListVirusScanTaskStatusesResponseBodyTasks] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of execution progress for virus scan tasks.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListVirusScanTaskStatusesResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class ListVirusScanTaskStatusesResponseBodyTasks(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        task_status: main_models.ListVirusScanTaskStatusesResponseBodyTasksTaskStatus = None,
    ):
        # The virus scan task ID.
        self.task_id = task_id
        # The execution progress measured by device count.
        self.task_status = task_status

    def validate(self):
        if self.task_status:
            self.task_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            temp_model = main_models.ListVirusScanTaskStatusesResponseBodyTasksTaskStatus()
            self.task_status = temp_model.from_map(m.get('TaskStatus'))

        return self

class ListVirusScanTaskStatusesResponseBodyTasksTaskStatus(DaraModel):
    def __init__(
        self,
        device_ack_count: int = None,
        device_result_fail_count: int = None,
        device_result_success_count: int = None,
        device_start_count: int = None,
    ):
        # The number of user terminal devices that have received the task.
        self.device_ack_count = device_ack_count
        # The number of user terminal devices on which the scan execution failed.
        self.device_result_fail_count = device_result_fail_count
        # The number of user terminal devices on which the scan was executed successfully.
        self.device_result_success_count = device_result_success_count
        # The number of user terminal devices that are currently executing the scan.
        self.device_start_count = device_start_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_ack_count is not None:
            result['DeviceAckCount'] = self.device_ack_count

        if self.device_result_fail_count is not None:
            result['DeviceResultFailCount'] = self.device_result_fail_count

        if self.device_result_success_count is not None:
            result['DeviceResultSuccessCount'] = self.device_result_success_count

        if self.device_start_count is not None:
            result['DeviceStartCount'] = self.device_start_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceAckCount') is not None:
            self.device_ack_count = m.get('DeviceAckCount')

        if m.get('DeviceResultFailCount') is not None:
            self.device_result_fail_count = m.get('DeviceResultFailCount')

        if m.get('DeviceResultSuccessCount') is not None:
            self.device_result_success_count = m.get('DeviceResultSuccessCount')

        if m.get('DeviceStartCount') is not None:
            self.device_start_count = m.get('DeviceStartCount')

        return self

