# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListAgentMJobInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAgentMJobInfoResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Other values indicate failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The returned data.
        self.data = data
        # The error message, if an error occurs.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: The request was successful.
        # - false/null: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAgentMJobInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAgentMJobInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        data_end_time: str = None,
        data_start_time: str = None,
        id: int = None,
        message: str = None,
        status: str = None,
        task_end_time: str = None,
        task_id: str = None,
        task_start_time: str = None,
    ):
        # The end time of the scan range.
        self.data_end_time = data_end_time
        # The start time of the scan range.
        self.data_start_time = data_start_time
        # The task ID.
        self.id = id
        # The error message, if an error occurs.
        self.message = message
        # The task status. Valid values:
        # 
        # - queing: The task is queued.
        # - readyAnalysis: The task is pending analysis.
        # - running: The task is running.
        # - error: The task failed.
        # - finish: The task is complete.
        # - fileUploadUser: The user-specified file is uploaded.
        # - fileUploadSystem: The system-generated file is uploaded.
        # - expired: The task has expired.
        self.status = status
        # The actual end time of the task.
        self.task_end_time = task_end_time
        # The scheduled task ID.
        self.task_id = task_id
        # The actual start time of the task.
        self.task_start_time = task_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_end_time is not None:
            result['DataEndTime'] = self.data_end_time

        if self.data_start_time is not None:
            result['DataStartTime'] = self.data_start_time

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataEndTime') is not None:
            self.data_end_time = m.get('DataEndTime')

        if m.get('DataStartTime') is not None:
            self.data_start_time = m.get('DataStartTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        return self

