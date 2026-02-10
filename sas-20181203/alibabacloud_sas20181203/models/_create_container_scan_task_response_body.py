# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateContainerScanTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateContainerScanTaskResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateContainerScanTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateContainerScanTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        can_create: bool = None,
        collect_time: int = None,
        exec_time: int = None,
        finish_count: int = None,
        progress: int = None,
        result: str = None,
        status: str = None,
        task_id: str = None,
        total_count: int = None,
    ):
        # Indicates whether you can create more scan tasks.
        self.can_create = can_create
        # The collection time.
        self.collect_time = collect_time
        # The execution time of the task.
        self.exec_time = exec_time
        # The number of scan tasks that are complete.
        self.finish_count = finish_count
        # The progress of the task.
        self.progress = progress
        # The execution result of the task.
        self.result = result
        # The status of the task.
        self.status = status
        # The ID of the task.
        self.task_id = task_id
        # The total number of scan tasks.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_create is not None:
            result['CanCreate'] = self.can_create

        if self.collect_time is not None:
            result['CollectTime'] = self.collect_time

        if self.exec_time is not None:
            result['ExecTime'] = self.exec_time

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.result is not None:
            result['Result'] = self.result

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanCreate') is not None:
            self.can_create = m.get('CanCreate')

        if m.get('CollectTime') is not None:
            self.collect_time = m.get('CollectTime')

        if m.get('ExecTime') is not None:
            self.exec_time = m.get('ExecTime')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

