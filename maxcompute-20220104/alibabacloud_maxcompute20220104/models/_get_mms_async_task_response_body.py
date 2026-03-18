# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetMmsAsyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMmsAsyncTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # The asynchronous task object.
        self.data = data
        # The request ID.
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetMmsAsyncTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMmsAsyncTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        error_msg: str = None,
        id: int = None,
        object_id: int = None,
        progress: int = None,
        result: str = None,
        running: bool = None,
        source_id: int = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The time when the task stopped running.
        self.end_time = end_time
        # The error message.
        self.error_msg = error_msg
        # The asynchronous task ID.
        self.id = id
        # The ID of the object associated with the asynchronous task.
        self.object_id = object_id
        # The progress of the task.
        self.progress = progress
        # The result of the task.
        self.result = result
        # Indicates whether the task is running.
        self.running = running
        # The data source ID.
        self.source_id = source_id
        # The time when the task started to run.
        self.start_time = start_time
        # The status of the asynchronous task.
        self.status = status
        # The type of the asynchronous task.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.id is not None:
            result['id'] = self.id

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.progress is not None:
            result['progress'] = self.progress

        if self.result is not None:
            result['result'] = self.result

        if self.running is not None:
            result['running'] = self.running

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('running') is not None:
            self.running = m.get('running')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

