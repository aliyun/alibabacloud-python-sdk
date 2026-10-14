# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOptimizeTaskResponseBody(DaraModel):
    def __init__(
        self,
        optimize_task_name: str = None,
        request_id: str = None,
    ):
        # The name of the optimization task.
        self.optimize_task_name = optimize_task_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.optimize_task_name is not None:
            result['optimizeTaskName'] = self.optimize_task_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('optimizeTaskName') is not None:
            self.optimize_task_name = m.get('optimizeTaskName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

