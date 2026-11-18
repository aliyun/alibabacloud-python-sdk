# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTaskDispatchStatusRequest(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The task ID. It is the unique identifier of the log configuration modification task. You can obtain the task ID from the TaskId parameter in the response of the ModifySlsDispatchConfig operation.
        # 
        # **Note**: This parameter is required. If it is not provided, the server returns a 400 error and rejects the request. Make sure to specify a valid TaskId.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

