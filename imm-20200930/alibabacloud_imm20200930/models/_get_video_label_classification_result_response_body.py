# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GetVideoLabelClassificationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        labels: List[main_models.Label] = None,
        message: str = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # The error code of the task.
        self.code = code
        # The end time of the task.
        self.end_time = end_time
        # The event ID.
        self.event_id = event_id
        # The labels.
        self.labels = labels
        # The error message of the task.
        self.message = message
        # The project name.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The start time of the task.
        self.start_time = start_time
        # The task status.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The type of the task.
        self.task_type = task_type
        # The custom information.
        self.user_data = user_data

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_id is not None:
            result['EventId'] = self.event_id

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

