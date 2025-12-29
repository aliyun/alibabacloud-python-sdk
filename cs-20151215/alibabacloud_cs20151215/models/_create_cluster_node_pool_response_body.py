# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClusterNodePoolResponseBody(DaraModel):
    def __init__(
        self,
        nodepool_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The request ID.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

