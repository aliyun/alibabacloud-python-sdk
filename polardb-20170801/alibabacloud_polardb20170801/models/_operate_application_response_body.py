# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateApplicationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The asynchronous task ID. For Ray restart, the parent task ID of restart_ray_cluster is returned. For DisableHeadScheduling and EnableHeadScheduling, the modify_ray_head_scheduling task ID is returned. A success response only indicates that the request is accepted. Historical applications or MCP paths may not return a task ID, and the default output is 0, which does not represent a valid task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

