# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_tingwu20230930 import models as main_models
from darabonba.model import DaraModel

class CreateTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        meeting_join_url: str = None,
        task_id: str = None,
        task_key: str = None,
        task_status: str = None,
    ):
        self.meeting_join_url = meeting_join_url
        self.task_id = task_id
        self.task_key = task_key
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meeting_join_url is not None:
            result['MeetingJoinUrl'] = self.meeting_join_url

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_key is not None:
            result['TaskKey'] = self.task_key

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeetingJoinUrl') is not None:
            self.meeting_join_url = m.get('MeetingJoinUrl')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

