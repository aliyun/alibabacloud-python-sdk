# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMemoryNodeResponseBody(DaraModel):
    def __init__(
        self,
        memory_node_id: str = None,
        request_id: str = None,
    ):
        self.memory_node_id = memory_node_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_node_id is not None:
            result['memoryNodeId'] = self.memory_node_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryNodeId') is not None:
            self.memory_node_id = m.get('memoryNodeId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

