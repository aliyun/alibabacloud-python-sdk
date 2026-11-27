# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopMPUTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        owner_id: int = None,
        task_id: str = None,
    ):
        # The application ID. Only a single ID can be passed.
        # 
        # > You can create and query the application ID in the [console](https://rtc.console.aliyun.com/manage/list#/manage/list).
        # 
        # This parameter is required.
        self.app_id = app_id
        self.owner_id = owner_id
        # The task ID. Only a single ID can be passed. The value must be the same as the TaskId parameter of [StartMpuTask](https://help.aliyun.com/document_detail/93183.html).
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

