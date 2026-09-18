# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsTaskLogsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMmsTaskLogsResponseBodyData] = None,
        request_id: str = None,
    ):
        # A list of logs.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListMmsTaskLogsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMmsTaskLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        action: str = None,
        create_time: str = None,
        id: int = None,
        msg: str = None,
        source_id: int = None,
        status: str = None,
        task_id: int = None,
    ):
        # The operation performed by the migration task.
        self.action = action
        # The time when the log was created.
        self.create_time = create_time
        # The log ID.
        self.id = id
        # The result of the migration task operation.
        self.msg = msg
        # The data source ID.
        self.source_id = source_id
        # The migration task status.
        self.status = status
        # The migration task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.msg is not None:
            result['msg'] = self.msg

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

