# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class PublicCreateImageScanTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.PublicCreateImageScanTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned when the operation is successful.
        self.data = data
        # The request ID. Alibaba Cloud generates a unique identifier for each request. You can use the request ID to troubleshoot issues.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.PublicCreateImageScanTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PublicCreateImageScanTaskResponseBodyData(DaraModel):
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
        # Indicates whether more scan tasks can be created. Valid values:
        # 
        # - **true**: More scan tasks can be created.
        # - **false**: No more scan tasks can be created.
        # 
        # > By default, up to 10 scan tasks can exist at the same time. If the number of scan tasks exceeds 10, creating a scan task by calling this operation fails. Wait until an existing scan task is completed before creating a new scan task.
        self.can_create = can_create
        # The timestamp when image information was collected, in milliseconds.
        self.collect_time = collect_time
        # The timestamp when the scan task started running, in milliseconds.
        self.exec_time = exec_time
        # The number of images that have been scanned.
        self.finish_count = finish_count
        # The progress percentage of the scan task.
        self.progress = progress
        # The execution result of the scan task. Valid values:
        # 
        # - **SUCCESS**: The scan task succeeded.
        # - **TASK_NOT_SUPPORT_REGION**: The image is in a region that does not support scanning.
        # 
        # > For the regions that support image security scanning, see the table of supported regions after the response parameters table in this topic.
        self.result = result
        # The status of the scan task. Valid values:
        # 
        # - **INIT**: Initializing.
        # - **PRE_ANALYZER**: Pre-analyzing.
        # - **SUCCESS**: Succeeded.
        # - **FAIL**: Failed.
        self.status = status
        # The ID of the scan task.
        self.task_id = task_id
        # The total number of images to scan.
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

